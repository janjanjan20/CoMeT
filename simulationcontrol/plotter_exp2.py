import matplotlib.pyplot as plt
import numpy as np




def calc_diff_dnape(arr_2d, arr_3d):
    if len(arr_2d) != len(arr_3d):
        print("Not the same length arrays given to calc_diff")
        return [0, 0]
    
    # difference = []
    percentage_of_2d = []
    for i in range(0, len(arr_2d)):
        percentage_of_2d.append(arr_3d[i] / arr_2d[i] * 100)

    return [np.mean(percentage_of_2d), np.std(percentage_of_2d)]


def calc_diff(arr_2d, arr_3d):
    if len(arr_2d) != len(arr_3d):
        print("Not the same length arrays given to calc_diff")
        return []
    
    # difference = []
    percentage_of_2d = []
    for i in range(0, len(arr_2d)):
        percentage_of_2d.append(arr_3d[i] / arr_2d[i] * 100)

    return percentage_of_2d


if __name__ == '__main__':
    dict_dnape = {
        "medium_blackscholes_2D_time": [77682647, 71626982, 73752892, 76349814], # in ns 74,853,083
        "medium_blackscholes_2D_peak_temp": 67.84,
                                       
        "medium_blackscholes_3D_time": [78382665, 75913039, 74253166, 74607079], # in ns 75,788,987
        "medium_blackscholes_3D_peak_temp": 66.14,
        # ----------------------------------------
                  
        "medium_bodytrack_2D_time": [186590178,  166610501,  162920523,  166027358], # in ns 170,537,140
        "medium_bodytrack_2D_peak_temp": 69.5,
                                       
        "medium_bodytrack_3D_time": [164945810, 164857982, 163832752, 165171598], # in ns 164,702,035
        "medium_bodytrack_3D_peak_temp": 69.66,
        # ----------------------------------------

        "medium_streamcluster_2D_time": [252506108, 218150340, 217173096, 222136134], # in ns 227,491,419
        "medium_streamcluster_2D_peak_temp": 66.4,
                                       
        "medium_streamcluster_3D_time": [240051452, 229824147, 218281059, 222653891], # in ns 227,702,637
        "medium_streamcluster_3D_peak_temp": 66.49,
        # ----------------------------------------

        "medium_swaptions_2D_time": [216483391, 167524392, 146343988, 145090942], # in ns 168,860,678
        "medium_swaptions_2D_peak_temp": 66.54,
                                       
        "medium_swaptions_3D_time": [194117788, 170200968, 148014083, 148161446], # in ns 165,123,571 
        "medium_swaptions_3D_peak_temp": 68.42,
        # ----------------------------------------

        "large_barnes_2D_time": [271918399, 253188903, 253953908, 256664481], # in ns 258,931,422 
        "large_barnes_2D_peak_temp": 65.4,
                                       
        "large_barnes_3D_time": [272767738, 252680235, 253841519, 257304973], # in ns 259,148,616
        "large_barnes_3D_peak_temp": 66.2,
        # ----------------------------------------

        "large_radiosity_2D_time": [401813606, 322055445, 314321630, 318033606], # in ns 339,056,071
        "large_radiosity_2D_peak_temp": 66.61,
                                       
        "large_radiosity_3D_time": [333242003, 325937392, 313266384, 315947570], # in ns 322,098,337
        "large_radiosity_3D_peak_temp": 66.72,
        # ----------------------------------------

        "large_raytrace_2D_time": [413163029, 409993493, 399206657, 416758858], # in ns 409,780,509 
        "large_raytrace_2D_peak_temp": 66.39,
                                       
        "large_raytrace_3D_time": [397829566, 403433718, 403581751, 410321490], # in ns 403,791,631
        "large_raytrace_3D_peak_temp": 66.37,
        # ----------------------------------------

        "large_water.nsq_2D_time": [346490470, 260227483, 236810462, 234577357], # in ns 269,526,443
        "large_water.nsq_2D_peak_temp": 69.24,
                                       
        "large_water.nsq_3D_time": [261099739, 240903028, 234676967, 232984662], # in ns 242,416,099
        "large_water.nsq_3D_peak_temp": 67.66,
        # ----------------------------------------

    }

    barWidth = 0.33
    br1 = np.arange(8) 
    br2 = [x + barWidth for x in br1] 

    benchmarks =  ["medium_blackscholes", "medium_bodytrack", "medium_streamcluster", "medium_swaptions", "large_barnes", "large_radiosity", "large_raytrace", "large_water.nsq"]
    benchmark_titles =  ["Blackscholes (M)", "Bodytrack (M)", "Streamcluster (M)", "Swaptions (M)", "Barnes (L)", "Radiosity (L)", "Raytrace (L)", "Water.nsq (L)"]
    time_res = []
    time_std = []
    temperature = []

    for x in benchmarks:
        res =  calc_diff_dnape(dict_dnape[x + '_2D_time'], dict_dnape[x + '_3D_time'])
        time_res.append(res[0])
        time_std.append(res[1])

        temperature.append(dict_dnape[x + '_3D_peak_temp'] / dict_dnape[x + '_2D_peak_temp'] * 100)


    fig = plt.subplots(figsize =(12, 8))

    plt.bar(br1, time_res, width=barWidth, label="Average execution time", hatch=".")
    plt.bar(br2, temperature, width=barWidth, label="Peak core temperature", hatch="/")
    plt.axhline(y = 100, color = 'gray', linestyle = '-', linewidth=0.5)


    plt.xlabel("Benchmarks")
    plt.ylabel("Percentage of 2D DNaPE (%)")
    plt.xticks([r + 0.48 * barWidth for r in range(8)], benchmark_titles)
    plt.legend()
    plt.ylim(75, 110)
    plt.show()



    fig = plt.subplots(figsize =(12, 8))
    titles = ["Streamcluster-0", "Streamcluster-1", "Streamcluster-2", "Streamcluster-3"]

    for x in ["medium_streamcluster_2D_time", "medium_streamcluster_3D_time"]:
        for i in range(0, 4):
            dict_dnape[x][i] = dict_dnape[x][i] / 1000000

    barWidth = 0.33
    br1 = np.arange(4) 
    br2 = [x + barWidth for x in br1]

    
    plt.bar(br1, dict_dnape['medium_streamcluster_2D_time'], width=barWidth, label="2D DNaPE", hatch=".")
    plt.bar(br2, dict_dnape['medium_streamcluster_3D_time'], width=barWidth, label="3D DNaPE", hatch="/")

    plt.xlabel("Tasks")
    plt.ylabel("Time (ms)")
    plt.xticks([r + 0.48 * barWidth for r in range(4)], titles)
    plt.legend()
    plt.ylim(0, 340)
    # plt.title("Peak temperature cores using DNaPE algorithms 32 active cores")
    plt.show()


#____________________________________________________________________________________________________________________________________
# date              config              tasks                                     avg resp time (ns)    resp times (ns)                                       peak core temperature
# ----------------  ------------------  ----------------------------------------  --------------------  --------------------------------------------------  -----------------------
# 2024-06-19_21.33  open+4.0GHz+dnape   bodytrack-simmedium-6_4times_2D           170,537,140           186,590,178  166,610,501  162,920,523  166,027,358                    69.5
# 2024-06-20_22.03  open+4.0GHz+dnape   bodytrack-simmedium-6_4times_3D           164,702,035           164,945,810  164,857,982  163,832,752  165,171,598                    69.66
# 2024-06-26_20.52  open+4.0GHz+dnape   blackscholes-simmedium-7_3D               75,788,987            78,382,665  75,913,039  74,253,166  74,607,079                        66.14
# 2024-06-26_20.52  open+4.0GHz+dnape   streamcluster-simmedium-7_3D              227,702,637           240,051,452  229,824,147  218,281,059  222,653,891                    66.49
# 2024-06-26_20.52  open+4.0GHz+dnape   swaptions-simmedium-7_3D                  165,123,571           194,117,788  170,200,968  148,014,083  148,161,446                    68.42
# 2024-06-27_11.46  open+4.0GHz+dnape   blackscholes-simmedium-7_2D               74,853,083            77,682,647  71,626,982  73,752,892  76,349,814                        67.84
# 2024-06-27_11.46  open+4.0GHz+dnape   streamcluster-simmedium-7_2D              227,491,419           252,506,108  218,150,340  217,173,096  222,136,134                    66.4
# 2024-06-27_11.46  open+4.0GHz+dnape   swaptions-simmedium-7_2D                  168,860,678           216,483,391  167,524,392  146,343,988  145,090,942                    66.54

# 2024-06-28_21.10  open+4.0GHz+dnape   barnes-large-8_2D                         258,931,422           271,918,399  253,188,903  253,953,908  256,664,481                    65.4
# 2024-06-28_21.10  open+4.0GHz+dnape   radiosity-large-8_2D                      339,056,071           401,813,606  322,055,445  314,321,630  318,033,606                    66.61
# 2024-06-28_21.10  open+4.0GHz+dnape   raytrace-large-8_2D                       409,780,509           413,163,029  409,993,493  399,206,657  416,758,858                    66.39
# 2024-06-30_10.55  open+4.0GHz+dnape   barnes-large-8_3D                         259,148,616           272,767,738  252,680,235  253,841,519  257,304,973                    66.2
# 2024-06-30_10.55  open+4.0GHz+dnape   radiosity-large-8_3D                      322,098,337           333,242,003  325,937,392  313,266,384  315,947,570                    66.72
# 2024-06-30_10.55  open+4.0GHz+dnape   raytrace-large-8_3D                       403,791,631           397,829,566  403,433,718  403,581,751  410,321,490                    66.37
# 2024-07-01_11.46  open+4.0GHz+dnape   water.nsq-large-8_3D                      242,416,099           261,099,739  240,903,028  234,676,967  232,984,662                    67.66
# 2024-07-01_22.14  open+4.0GHz+dnape   water.nsq-large-8_2D                      269,526,443           346,490,470  260,227,483  236,810,462  234,577,357                    69.24

# 2024-06-25_13.37  open+4.0GHz+dnape3  bodytrack-simmedium-6_3D_YES              160,183,124           160,809,677  160,702,304  159,037,418  160,183,097                    69.5
# 2024-06-26_15.06  open+4.0GHz+dnape3  blackscholes-simmedium-7_ugh_accident...  73,743,169            76,002,696  74,709,778  72,908,464  71,351,738                        66.32
