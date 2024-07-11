import os
from tabulate import tabulate
from resultlib import *

def main():
    headers = [
        'date',
        'config',
        'tasks',
        #'sim. time (ns)',
        'avg resp time (ns)',
        'resp times (ns)',
        'peak core temperature',
    ]
    rows = []
    runs = sorted(list(get_runs()))
    for run in runs:
        if has_properly_finished(run):
            config = get_config(run)
            tasks = get_tasks(run)
            if len(tasks) > 40:
                tasks = tasks[:37] + '...'
            rows.append([
                get_date(run),
                config,
                tasks,
                #'{:,}'.format(get_total_simulation_time(run)),
                '{:,}'.format(get_average_response_time(run)),
                '  '.join('{:,}'.format(r) for r in get_individual_response_times(run)),
                max(get_core_peak_temperature_traces(run)[0]),
            ])
    print(tabulate(rows, headers=headers))
    
    print([rows[i][4] for i in range(0, len(rows))])
    print([rows[i][5] for i in range(0, len(rows))])


if __name__ == '__main__':
    main()
