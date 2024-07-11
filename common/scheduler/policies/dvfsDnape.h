/**
 * This header implements the dnape governer
 */

#ifndef __DVFS_DVFSDNAPE_H
#define __DVFS_DVFSDNAPE_H

#include <vector>
#include "dvfspolicy.h"
#include "performance_counters.h"

class DVFSDnape : public DVFSPolicy {
public:
    DVFSDnape(
        const PerformanceCounters *performanceCounters,
        int numberOfCores,
        int minFrequency,
        int maxFrequency,
        int frequencyStepSize,
        float criticalTemperature,
        float alfa,
        float freqThreshold,
        float delta);
    virtual std::vector<int> getFrequencies(const std::vector<int> &oldFrequencies, const std::vector<bool> &activeCores);

private:
    const PerformanceCounters *performanceCounters;

    unsigned int numberOfCores;
    int minFrequency;
    int maxFrequency;
    int frequencyStepSize;
    float criticalTemperature;
    float alfa;
    float freqThreshold;
    float delta;

    bool in_throttle_mode = false;
    bool throttle();
};

#endif
