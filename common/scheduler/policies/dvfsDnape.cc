#include "dvfsDnape.h"
#include <iomanip>
#include <iostream>

using namespace std;

DVFSDnape::DVFSDnape(
        const PerformanceCounters *performanceCounters,
        int numberOfCores,
        int minFrequency,
        int maxFrequency,
        int frequencyStepSize,
        float criticalTemperature,
        float alfa,
        float freqThreshold,
        float delta)
    : performanceCounters(performanceCounters),
      numberOfCores(numberOfCores),
      minFrequency(minFrequency),
      maxFrequency(maxFrequency),
      frequencyStepSize(frequencyStepSize),
      criticalTemperature(criticalTemperature),
      alfa(alfa),
      freqThreshold(freqThreshold),
      delta(delta) {

}

std::vector<int> DVFSDnape::getFrequencies(const std::vector<int> &oldFrequencies, const std::vector<bool> &activeCores) {
    std::vector<int> frequencies(numberOfCores);

    for (unsigned int coreCounter = 0; coreCounter < numberOfCores; coreCounter++) {
        if (activeCores.at(coreCounter)) {
            float power = performanceCounters->getPowerOfCore(coreCounter);
            float temperature = performanceCounters->getTemperatureOfCore(coreCounter);
            int frequency = oldFrequencies.at(coreCounter);
            float utilization = performanceCounters->getUtilizationOfCore(coreCounter);

            cout << "[Scheduler][dvfsDnape]: Core " << setw(2) << coreCounter << ":";
            cout << " P=" << fixed << setprecision(3) << power << " W";
            cout << "  f=" << frequency << " MHz";
            cout << "  T=" << fixed << setprecision(1) << temperature << " C";  // avoid the '°' symbol, it is not ASCII
            cout << "  utilization=" << fixed << setprecision(3) << utilization << endl;

            // Increase frequency if temperature is more than alfa below critical,
            // and the current frequency is below the frequency threshold.
            if (temperature < criticalTemperature - alfa && frequency < freqThreshold) {
                cout << "[Scheduler][dvfsDnape]: Current temperature more than alfa below max";
                if (frequency == maxFrequency) {
                    cout << " but already at max frequency" << endl;
                } else {
                    cout << " -> increase frequency with delta" << endl;
                    frequency = frequency + delta;
                    if (frequency > maxFrequency) {
                        frequency = maxFrequency;
                    }
                }
            // Decrease frequency if temperature above critical.
            } else if (temperature > criticalTemperature) {
                cout << "[Scheduler][dvfsDnape]: Current temeprature of core is too high!!";
                if (frequency == minFrequency) {
                    cout << " but already at min frequency" << endl;
                } else {
                    cout << " -> lower frequency with delta" << endl;
                    frequency = frequency - delta;
                    if (frequency < minFrequency) {
                        frequency = minFrequency;
                    }
                }
            }

            frequencies.at(coreCounter) = frequency;
        } else {
            // frequencies.at(coreCounter) = minFrequency;
            frequencies.at(coreCounter) = oldFrequencies.at(coreCounter);
        }
    }
    return frequencies;
}
