import matplotlib.pyplot as plt
import numpy as np




def calc_diff(arr_2d, arr_3d, is_temp):
    if len(arr_2d) != len(arr_3d):
        print("Not the same length arrays given to calc_diff")
        return []
    
    # difference = []
    percentage_of_2d = []
    for i in range(0, len(arr_2d)):
        diff = arr_2d[i] - arr_3d[i]
        # difference.append(diff)
        if is_temp:
            diff = diff * -1
        percentage_of_2d.append(diff / arr_2d[i] * 100)

    return percentage_of_2d




if __name__ == '__main__':
    # all with freq 3.0 GHz and cores: 4, 8, 12, 16
    dict = {
        # The 4x4x4
        "blackscholes_4L_time": [29429826, 23181462, 21275069, 20542798],
        "blackscholes_4L_temp": [55.64, 54.81, 54.14, 54.02],

        "bodytrack_4L_time": [159942426, 66630916, 47891349, 40204835],
        "bodytrack_4L_temp": [61.06, 60.65, 60.79, 60.33],

        "streamcluster_4L_time": [112407255, 58112104, 46981443, 45162412],
        "streamcluster_4L_temp": [57.91, 58.01, 57.9, 57.65],

        "swaptions_4L_time": [64859648, 42701418, 64515338, 21487064],
        "swaptions_4L_temp": [59.05, 58.11, 55.89, 55.89],

        "barnes_4L_time": [284459245, 148273514, 100620577, 77237305],
        "barnes_4L_temp": [57.3, 57.56, 57.88, 57.58],


        "radiosity_4L_time": [132659969, 62497990, 44849013, 38509442],
        "radiosity_4L_temp": [57.03, 57.12, 57.45, 57.7],

        "raytrace_4L_time": [421883757, 370324242, 358001913, 338173830],
        "raytrace_4L_temp": [59.01, 59.66, 60.04, 59.84],

        "water.nsq_4L_time": [39921646, 25807293, 23700467, 21483889],
        "water.nsq_4L_temp": [56.85, 56.6, 55.93, 55.75],


        # The 8x8x1
        "blackscholes_8L_time": [30155498, 24354802, 23077741, 22390433],
        "blackscholes_8L_temp": [48.23, 48.03, 47.78, 47.55],

        # 16 cores gave an error due to deadlock: *ERROR* No threads running, no timeout. Application has deadlocked...
        # Did succeed the third time..
        "bodytrack_8L_time": [170570277, 70525158, 50519616, 42151307 ],
        "bodytrack_8L_temp": [50.2, 49.99, 49.9, 49.88],

        "streamcluster_8L_time": [121438305, 62513457, 47721898, 45653705],
        "streamcluster_8L_temp": [48.1, 48.09, 48.1, 48.11],

        "swaptions_8L_time": [66131155, 43811020, 66111532, 22310825],
        "swaptions_8L_temp": [48.57, 48.57, 48.28, 48.25],

        "barnes_8L_time": [303920684, 157596635, 107077475, 82690401],
        "barnes_8L_temp": [47.37, 47.46, 47.35, 47.33],


        "radiosity_8L_time": [143272095, 64254085, 47530464, 40318909],
        "radiosity_8L_temp": [47.56, 47.7, 47.72, 48.02],

        "raytrace_8L_time": [424908457, 405988522, 391411404, 372781647],
        "raytrace_8L_temp": [48.3, 48.26, 48.66, 48.37],

        "water.nsq_8L_time": [41631624, 26890506, 24991930, 21871604],
        "water.nsq_8L_temp": [48.08, 47.97, 47.83, 47.67],


        #######################################################################################################
        # Coldest core 4x4x4
        "cold_blackscholes_4L_time": [29913781, 24610336, 20869458, 19980827],
        "cold_blackscholes_4L_temp": [52.28, 51.62, 51.22, 52.19],


        "cold_bodytrack_4L_time": [158554413, 66036622, 47524360],
        "cold_bodytrack_4L_temp": [55.85, 54.87, 54.48],
    }

    
    



    benchmarks = ["blackscholes", "bodytrack", "streamcluster", "swaptions", "barnes", "radiosity", "raytrace", "water.nsq"]
    benchmark_names = ["Blackscholes", "Bodytrack", "Streamcluster", "Swaptions", "Barnes", "Radiosity", "Raytrace", "Water.nsq"]
    cores = [4, 8, 12, 16]

    # Set position of bar on X axis 
    barWidth = 0.33
    br1 = np.arange(4) 
    br2 = [x + barWidth for x in br1] 

    for bench in benchmarks:
        time_diff = calc_diff(dict[bench + "_8L_time"], dict[bench + "_4L_time"], False)
        temp_diff = calc_diff(dict[bench + "_8L_temp"], dict[bench + "_4L_temp"], True)

        fig = plt.subplots(figsize =(12, 8))

        plt.bar(br1, time_diff, width = barWidth, label="Time decrease for 3D", hatch=".")
        plt.bar(br2, temp_diff, width = barWidth, label="Temperature increase for 3D", hatch="/")
        plt.xlabel("Active cores")
        plt.ylabel("Percentage of 2D results")
        plt.xticks([r + 0.48 * barWidth for r in range(4)], 
            ['4', '8', '12', '16'])
        plt.legend()
        plt.ylim(0, 25)
        #plt.title("Results worst cores " + bench + " with freq 3.0 GHz")
        plt.show()

    # Create the plot with all the different benchmarks and their percentage
    # Set position of bar on X axis 
    barWidth = 0.33
    br1 = np.arange(8) 
    br2 = [x + barWidth for x in br1]


    for i in range(0, 4):
        all_times = []
        all_temps = []
        for bench in benchmarks:
            time_diff = calc_diff(dict[bench + "_8L_time"], dict[bench + "_4L_time"], False)
            temp_diff = calc_diff(dict[bench + "_8L_temp"], dict[bench + "_4L_temp"], True)

            all_times.append(time_diff[i])
            all_temps.append(temp_diff[i])

            # plt.plot(cores, time_diff, label="Time decrease for 3D", marker="o")
            # plt.plot(cores, temp_diff, label="Temperature increase for 3D", marker="o")

        fig = plt.subplots(figsize =(12, 8))

        plt.bar(br1, all_times, width = barWidth, label="Time decrease for 3D", hatch=".")
        plt.bar(br2, all_temps, width = barWidth, label="Temperature increase for 3D", hatch="/")
        plt.xlabel("Benchmarks")
        plt.ylabel("Difference with 2D (%)")
        plt.xticks([r + 0.48 * barWidth for r in range(8)], benchmark_names)
        plt.legend()
        # plt.title("Results worst cores " + bench + " with freq 3.0 GHz")
        plt.show()


    # ---------------------------------------------------------------------------------------------------------------------
    # fig = plt.subplots(figsize =(12, 8))
    # barWidth = 0.25
    # br1 = np.arange(4) 
    # br2 = [x + barWidth for x in br1]
    # br3 = [x + 2 * barWidth for x in br1]

    # plt.bar(br1, dict['cold_blackscholes_4L_time'], width = barWidth, label="Time coldest cores 3D")
    # plt.bar(br2, dict['blackscholes_4L_time'], width = barWidth, label="Time worst cores 3D")
    # plt.bar(br3, dict['blackscholes_8L_time'], width = barWidth, label="Time worst cores 2D")
    # plt.xlabel("Active cores")
    # plt.ylabel("Time (ns)")
    # plt.xticks([r + 0.48 * barWidth for r in range(4)], 
    #     ['4', '8', '12', '16'])
    # plt.legend()
    # plt.title("Blackscholes time coldest cores with freq 3.0 GHz")
    # plt.show()


    # fig = plt.subplots(figsize =(12, 8))
    # plt.bar(br1, dict['cold_blackscholes_4L_temp'], width = barWidth, label="Temperature coldest cores 3D")
    # plt.bar(br2, dict['blackscholes_4L_temp'], width = barWidth, label="Temperature worst cores 3D")
    # plt.bar(br3, dict['blackscholes_8L_temp'], width = barWidth, label="Temperature worst cores 2D")
    # plt.xlabel("Active cores")
    # plt.ylabel("Temperature (C)")
    # plt.xticks([r + 0.48 * barWidth for r in range(4)], 
    #     ['4', '8', '12', '16'])
    # plt.ylim(45, 60)
    # plt.legend()
    # plt.title("Blackscholes temperature coldest cores with freq 3.0 GHz")
    # plt.show()





    

# date              config                 tasks                      avg resp time (ns)    resp times (ns)      peak core temperature
# ----------------  ---------------------  -------------------------  --------------------  -----------------  -----------------------
# #4x4x4
# 2024-05-13_09.10  open+3.0GHz+constFreq  blackscholes-simsmall-11   21,275,069            21,275,069                           54.14
# 2024-05-13_09.10  open+3.0GHz+constFreq  blackscholes-simsmall-15   20,542,798            20,542,798                           54.02
# 2024-05-13_09.10  open+3.0GHz+constFreq  blackscholes-simsmall-3    29,429,826            29,429,826                           55.64
# 2024-05-13_09.10  open+3.0GHz+constFreq  blackscholes-simsmall-7    23,181,462            23,181,462                           54.81

# 2024-05-13_09.10  open+3.0GHz+constFreq  bodytrack-simsmall-2       159,942,426           159,942,426                          61.06
# 2024-05-13_09.10  open+3.0GHz+constFreq  bodytrack-simsmall-6       66,630,916            66,630,916                           60.65
# 2024-05-13_09.10  open+3.0GHz+constFreq  bodytrack-simsmall-10      47,891,349            47,891,349                           60.79
# 2024-05-13_09.10  open+3.0GHz+constFreq  bodytrack-simsmall-14      40,204,835            40,204,835                           60.33

# 2024-05-13_22.38  open+3.0GHz+constFreq  streamcluster-simsmall-3   112,407,255           112,407,255                          57.91
# 2024-05-13_22.38  open+3.0GHz+constFreq  streamcluster-simsmall-7   58,112,104            58,112,104                           58.01
# 2024-05-13_22.38  open+3.0GHz+constFreq  streamcluster-simsmall-11  46,981,443            46,981,443                           57.9
# 2024-05-13_22.38  open+3.0GHz+constFreq  streamcluster-simsmall-15  45,162,412            45,162,412                           57.65

# 2024-05-13_22.38  open+3.0GHz+constFreq  swaptions-simsmall-3       64,859,648            64,859,648                           59.05
# 2024-05-13_22.38  open+3.0GHz+constFreq  swaptions-simsmall-7       42,701,418            42,701,418                           58.11
# 2024-05-13_22.38  open+3.0GHz+constFreq  swaptions-simsmall-11      64,515,338            64,515,338                           55.89
# 2024-05-13_22.38  open+3.0GHz+constFreq  swaptions-simsmall-15      21,487,064            21,487,064                           55.89

# 2024-05-14_09.46  open+3.0GHz+constFreq  barnes-small-4             284,459,245           284,459,245                          57.3
# 2024-05-14_09.46  open+3.0GHz+constFreq  barnes-small-8             148,273,514           148,273,514                          57.56
# 2024-05-14_15.37  open+3.0GHz+constFreq  barnes-small-12            100,620,577           100,620,577                          57.88
# 2024-05-14_15.37  open+3.0GHz+constFreq  barnes-small-16            77,237,305            77,237,305                           57.58

# # 8x8x1 ------------------------------------------------------------------------------------------------------------------------------------------
# 2024-05-14_21.30  open+3.0GHz+constFreq  blackscholes-simsmall-3    30,155,498            30,155,498                           48.23
# 2024-05-14_21.30  open+3.0GHz+constFreq  blackscholes-simsmall-7    24,354,802            24,354,802                           48.03
# 2024-05-14_21.30  open+3.0GHz+constFreq  blackscholes-simsmall-11   23,077,741            23,077,741                           47.78
# 2024-05-14_21.30  open+3.0GHz+constFreq  blackscholes-simsmall-15   22,390,433            22,390,433                           47.55

# 2024-05-14_21.30  open+3.0GHz+constFreq  bodytrack-simsmall-2       170,570,277           170,570,277                          50.2
# 2024-05-14_21.30  open+3.0GHz+constFreq  bodytrack-simsmall-6       70,525,158            70,525,158                           49.99
# 2024-05-14_21.30  open+3.0GHz+constFreq  bodytrack-simsmall-10      50,519,616            50,519,616                           49.9

# 2024-05-14_21.30  open+3.0GHz+constFreq  streamcluster-simsmall-3   121,438,305           121,438,305                          48.1
# 2024-05-14_21.30  open+3.0GHz+constFreq  streamcluster-simsmall-7   62,513,457            62,513,457                           48.09
# 2024-05-14_21.30  open+3.0GHz+constFreq  streamcluster-simsmall-11  47,721,898            47,721,898                           48.1
# 2024-05-14_21.30  open+3.0GHz+constFreq  streamcluster-simsmall-15  45,653,705            45,653,705                           48.11

# 2024-05-14_21.30  open+3.0GHz+constFreq  swaptions-simsmall-3       66,131,155            66,131,155                           48.57
# 2024-05-14_21.30  open+3.0GHz+constFreq  swaptions-simsmall-7       43,811,020            43,811,020                           48.57
# 2024-05-14_21.30  open+3.0GHz+constFreq  swaptions-simsmall-11      66,111,532            66,111,532                           48.28
# 2024-05-14_21.30  open+3.0GHz+constFreq  swaptions-simsmall-15      22,310,825            22,310,825                           48.25

# 2024-05-15_07.25  open+3.0GHz+constFreq  barnes-small-4             303,920,684           303,920,684                          47.37
# 2024-05-15_10.01  open+3.0GHz+constFreq  barnes-small-8             157,596,635           157,596,635                          47.46
# 2024-05-15_10.01  open+3.0GHz+constFreq  barnes-small-12            107,077,475           107,077,475                          47.35
# 2024-05-15_10.01  open+3.0GHz+constFreq  barnes-small-16            82,690,401            82,690,401                           47.33
