/**
* This header implements the Dynamic Neighbor-Aware
* Performance Enhancement policy.
*/
#ifndef __DNAPE_H
#define __DNAPE_H
#include <vector>
#include "mappingpolicy.h"
#include "migrationpolicy.h"
#include "performance_counters.h"




class Dnape : public MappingPolicy, public MigrationPolicy {
public:
    Dnape(
        const PerformanceCounters *performanceCounters,
        int coresInX,
        int coresInY,
        int coresInZ,
        float criticalTemperature,
        float alfa,
        float freqThreshold,
        float delta,
        SubsecondTime wake_up_latency,
        bool use2D);
    virtual std::vector<int> map(
        String taskName,
        int taskCoreRequirement,
        const std::vector<bool> &availableCores,
        const std::vector<bool> &activeCores);
    virtual std::vector<migration> migrate(
        SubsecondTime time,
        const std::vector<int> &taskIds,
        const std::vector<bool> &activeCores);

private:
    const PerformanceCounters *performanceCounters;

    int coresInX;
    int coresInY;
    int coresInZ;
    float criticalTemperature;
    float alfa;
    float freqThreshold;
    float delta;
    SubsecondTime wake_up_latency;
    bool use2D;
    
    int getColdestCore(const std::vector<bool> &availableCores);
    int getColdestNeighbor(const std::vector<bool> &availableCores, const int currentCore);
    int getColdestNeighbor2D(const std::vector<bool> &availableCores, const int currentCore);
    int getBestNeighbor3D(const std::vector<bool> &availableCores, const int currentCore, const float currentTemperature);
    void computePosition(core_id_t core, SInt32 &x, SInt32 &y, SInt32 &z);
    core_id_t computeCoreId(SInt32 x, SInt32 y, SInt32 z);
    void logTemperatures(const std::vector<bool> &availableCores);
};
#endif