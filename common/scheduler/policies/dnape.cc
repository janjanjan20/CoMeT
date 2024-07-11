#include "dnape.h"
#include "simulator.h"
#include "core_manager.h"
#include "performance_model.h"
#include "instruction.h"

#include <iomanip>

using namespace std;

Dnape::Dnape(
        const PerformanceCounters *performanceCounters,
        int coresInX,
        int coresInY,
        int coresInZ,        
        float criticalTemperature,
        float alfa,
        float freqThreshold,
        float delta,
        SubsecondTime wake_up_latency,
        bool use2D)
    : performanceCounters(performanceCounters),
        coresInX(coresInX),
        coresInY(coresInY),
        coresInZ(coresInZ),
        criticalTemperature(criticalTemperature),
        alfa(alfa),
        freqThreshold(freqThreshold),
        delta(delta),
        wake_up_latency(wake_up_latency),
        use2D(use2D) {
    // m_transition_latency = SubsecondTime::NS() * Sim()->getCfg()->getInt("scheduler/open/migration/dnape/wake-up_latency");
}


std::vector<int> Dnape::map(
        String taskName,
        int taskCoreRequirement,
        const std::vector<bool> &availableCoresRO,
        const std::vector<bool> &activeCores) {

    std::vector<bool> availableCores(availableCoresRO);

    std::vector<int> cores;

    logTemperatures(availableCores);

    for (; taskCoreRequirement > 0; taskCoreRequirement--) {
        int coldestNeighbor = getColdestNeighbor(availableCores, taskCoreRequirement);
        if (coldestNeighbor == -1) {
            // not enough free cores
            std::vector<int> empty;
            return empty;
        } else {
            cores.push_back(coldestNeighbor);
            availableCores.at(coldestNeighbor) = false;
        }
    }

    return cores;
}


std::vector<migration> Dnape::migrate(
        SubsecondTime time,
        const std::vector<int> &taskIds,
        const std::vector<bool> &activeCores) {

    std::vector<migration> migrations;
    std::vector<bool> availableCores(coresInX * coresInY * coresInZ);
    for (int c = 0; c < coresInX * coresInY * coresInZ; c++) {
        availableCores.at(c) = taskIds.at(c) == -1;
    }

    for (int c = 0; c < coresInX * coresInY * coresInZ; c++) {
        if (activeCores.at(c)) {
            float currentTemperature = performanceCounters->getTemperatureOfCore(c);
            if (currentTemperature > criticalTemperature) {
                cout << "[Scheduler][dnape-migrate]: core" << c << " too hot(";
                cout << fixed << setprecision(1) << currentTemperature << ") -> migrate";
                logTemperatures(availableCores);

                int targetCore;
                if (use2D) {
                    targetCore = getColdestNeighbor2D(availableCores, c);
                } else {
                    targetCore = getColdestNeighbor(availableCores, c);
                }
                
                float targetTemp = performanceCounters->getTemperatureOfCore(targetCore);

                if (targetCore == -1) {
                    cout << "[Scheduler][dnape-migrate]: no target core found, cannot migrate" << endl;
                // Migrate if the temperature of the target is more than alfa below the threshold.
                } else if (targetTemp < criticalTemperature - alfa) {
                    migration m;
                    m.fromCore = c;
                    m.toCore = targetCore;
                    m.swap = false;
                    migrations.push_back(m);
                    availableCores.at(targetCore) = false;

                    /* queue a fake instruction that will account for the wake-up latency */
                    PseudoInstruction *i = new DelayInstruction(wake_up_latency, DelayInstruction::DVFS_TRANSITION);
                    Sim()->getCoreManager()->getCoreFromID(targetCore)->getPerformanceModel()->queuePseudoInstruction(i);
                    cout << "[Scheduler][dnape-migrate]: wake-up latency!" << endl;

                // Migrate if the temperature of the target is more than alfa below the
                // temperature of the current core. Also reduce the frequency.
                } else if (targetTemp < currentTemperature - alfa) {
                    migration m;
                    m.fromCore = c;
                    m.toCore = targetCore;
                    m.swap = false;
                    migrations.push_back(m);
                    availableCores.at(targetCore) = false;

                    cout << "[Scheduler][dnape-migrate]: Reduce frequency!" << endl;
                    cout << "[Scheduler][dnape-migrate]: Move to temperature: " << targetTemp << endl;

                    /* queue a fake instruction that will account for the wake-up latency */
                    PseudoInstruction *i = new DelayInstruction(wake_up_latency, DelayInstruction::DVFS_TRANSITION);
                    Sim()->getCoreManager()->getCoreFromID(c)->getPerformanceModel()->queuePseudoInstruction(i);
                    cout << "[Scheduler][dnape-migrate]: wake-up latency!" << endl;

                // Reduce the frequency of the current core otherwise.
                } else {
                    cout << "[Scheduler][dnape-migrate]: Reduce frequency!" << endl;
                }
            }
        }
    }
    return migrations;
}


int Dnape::getColdestCore(const std::vector<bool> &availableCores) {
    int coldestCore = -1;
    float coldestTemperature = 0;
    // iterate all cores to find coldest
    for (int c = 0; c < coresInX * coresInY * coresInZ; c++) {
        if (availableCores.at(c)) {
            float temperature = performanceCounters->getTemperatureOfCore(c);
            if ((coldestCore == -1) || (temperature < coldestTemperature)) {
                coldestCore = c;
                coldestTemperature = temperature;
            }
        }
    }
    return coldestCore;
}


int Dnape::getColdestNeighbor(const std::vector<bool> &availableCores, const int currentCore) {
    int coldestCore = -1;
    float coldestTemperature = 0;

    // Iterate all neighboring cores to find coldest
    for (int addX = -1; addX <= 1; addX++) {
        for (int addY = -1; addY <= 1; addY++) {
            for (int addZ = -1; addZ <= 1; addZ++) {
                int curX, curY, curZ;
                computePosition(currentCore, curX, curY, curZ);

                // Check whether the neighbor is inside the mesh grid
                if (curX + addX < coresInX && curY + addY < coresInY && curZ + addZ < coresInZ &&
                    curX + addX >= 0 && curY + addY >= 0 && curZ + addZ >= 0) {

                    int c = computeCoreId(curX + addX, curY + addY, curZ + addZ);
                    if (availableCores.at(c)) {
                        float temperature = performanceCounters->getTemperatureOfCore(c);
                        if ((coldestCore == -1) || (temperature < coldestTemperature)) {
                            coldestCore = c;
                            coldestTemperature = temperature;
                        }
                    }
                }
            }
        }
    }

    return coldestCore;
}


int Dnape::getColdestNeighbor2D(const std::vector<bool> &availableCores, const int currentCore) {
    int coldestCore = -1;
    float coldestTemperature = 0;

    // Iterate all neighboring cores to find coldest
    for (int addX = -1; addX <= 1; addX++) {
        for (int addY = -1; addY <= 1; addY++) {
            int curX, curY, curZ;
            computePosition(currentCore, curX, curY, curZ);

            // Check whether the neighbor is inside the mesh grid
            if (curX + addX < coresInX && curY + addY < coresInY &&
                curX + addX >= 0 && curY + addY >= 0) {

                int c = computeCoreId(curX + addX, curY + addY, curZ);
                if (availableCores.at(c)) {
                    float temperature = performanceCounters->getTemperatureOfCore(c);
                    if ((coldestCore == -1) || (temperature < coldestTemperature)) {
                        coldestCore = c;
                        coldestTemperature = temperature;
                    }
                }
            }

        }
    }

    return coldestCore;
}


void
Dnape::computePosition(core_id_t core_id, SInt32 &x, SInt32 &y, SInt32 &z)
{
    // Assuming the m_concectration is 1
    x = core_id % coresInX;
    y = core_id % (coresInX * coresInY) / coresInX;
    z = core_id / (coresInX * coresInY);
}

core_id_t
Dnape::computeCoreId(SInt32 x, SInt32 y, SInt32 z)
{
    // Assuming the m_concectration is 1
    x = (x + coresInX) % coresInX;
    y = (y + coresInY) % coresInY;
    z = (z + coresInZ) % coresInZ;
   return (z * coresInX * coresInY + y * coresInX + x);
}


void Dnape::logTemperatures(const std::vector<bool> &availableCores) {
    cout << "[Scheduler][dnape-map]: temperatures of available cores:" << endl;

    for (int z = 0; z < coresInZ; z++) {
        for (int y = 0; y < coresInY; y++) {
            for (int x = 0; x < coresInX; x++) {
                if (x > 0) {
                    cout << " ";
                }
                int coreId = z * coresInX * coresInY + y * coresInX + x;

                if (!availableCores.at(coreId)) {
                    cout << " - ";
                } else {
                    float temperature = performanceCounters->getTemperatureOfCore(
                        coreId);
                cout << fixed << setprecision(1) << temperature;
                }
            }
        cout << endl;
        }
        cout << endl;
        cout << endl;
    }
}