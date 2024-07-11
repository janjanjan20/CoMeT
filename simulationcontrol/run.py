import runlib


# 'parsec-blackscholes': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
# 'parsec-bodytrack': [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
# 'parsec-canneal': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
# 'parsec-dedup': [4, 7, 10, 13, 16],
# 'parsec-fluidanimate': [2, 3, 0, 5, 0, 0, 0, 9],
# 'parsec-streamcluster': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
# 'parsec-swaptions': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
# 'parsec-x264': [1, 3, 4, 5, 6, 7, 8, 9],
# 'splash2-barnes': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
# 'splash2-cholesky': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
# 'splash2-fft': [1, 2, 0, 4, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 16],
# 'splash2-fmm': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
# 'splash2-lu.cont': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
# 'splash2-lu.ncont': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
# 'splash2-ocean.cont': [1, 2, 0, 4, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 16],
# 'splash2-ocean.ncont': [1, 2, 0, 4, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 16],
# 'splash2-radiosity': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
# 'splash2-radix': [1, 2, 0, 4, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 16],
# 'splash2-raytrace': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
# 'splash2-water.nsq': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
# 'splash2-water.sp': [1, 2, 0, 4, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 16],

def example2():
    for benchmark in (
                      # 'parsec-blackscholes', #done 
                      #'parsec-bodytrack', #done
                      #'parsec-canneal',
                      #'parsec-dedup',
                      #'parsec-fluidanimate',
                      #'parsec-streamcluster', #done 
                      #'parsec-swaptions', #done 
                      #'parsec-x264',
                      #'splash2-barnes', #input_set = 'small' instead of 'simsmall #done 
                      #'splash2-fmm',
                      #'splash2-ocean.cont',
                      #'splash2-ocean.ncont',
                      #'splash2-radiosity', #done
                      #'splash2-raytrace', #done
                      'splash2-water.nsq', #done
                      #'splash2-water.sp',
                      ##'splash2-cholesky',
                      #'splash2-fft',
                      ##'splash2-lu.cont',
                      ##'splash2-lu.ncont',
                      #'splash2-radix'
                      ):
        # min_parallelism = runlib.get_feasible_parallelisms(benchmark)[0]
        # max_parallelism = runlib.get_feasible_parallelisms(benchmark)[-1]
        # for freq in (1, 2, 3, 4):
            # for parallelism in (min_parallelism, max_parallelism):

        freq = 4
        parallelism = 8
        #for parallelism in (4, 8, 12, 16):
            
        inp_set = 'large'
        benchmarks_string = f"{runlib.get_instance(benchmark, parallelism, input_set=inp_set)},{runlib.get_instance(benchmark, parallelism, input_set=inp_set)},{runlib.get_instance(benchmark, parallelism, input_set=inp_set)},{runlib.get_instance(benchmark, parallelism, input_set=inp_set)}"

        # The 'dnape' was 'constFreq
        # runlib.run(['open', '{:.1f}GHz'.format(freq), 'dnape'], runlib.get_instance(benchmark, parallelism, input_set=inp_set))
        # runlib.run(['open', '{:.1f}GHz'.format(freq), 'dnape'], benchmarks_string)

        runlib.run(['open', '{:.1f}GHz'.format(freq), 'dnape'], benchmarks_string)
        # runlib.run(['open', '{:.1f}GHz'.format(freq), 'dnape2'], benchmarks_string)
        # runlib.run(['{:.1f}GHz'.format(freq)], 'parsec-blackscholes-small-16,parsec-blackscholes-small-16')

        # parallelism = 16
        # benchmarks_string2 = f"{runlib.get_instance(benchmark, parallelism, input_set=inp_set)},{runlib.get_instance(benchmark, parallelism, input_set=inp_set)}"
        # runlib.run(['open', '{:.1f}GHz'.format(freq), 'dnape'], benchmarks_string2)


def example():
    # for freq in (1, 2, 3, 4):  # when adding a new frequency level, make sure that it is also added in base.cfg

    freq = 4
    runlib.run(['open', '{:.1f}GHz'.format(freq)], {'parsec-blackscholes-simmedium-11', 'parsec-blackscholes-simmedium-15'})


def case_study():
    runlib.run(['open', 'ondemand'], runlib.get_instance('parsec-swaptions', parallelism=4, input_set='medium'))


def main():
    example2()
    # example2()
    # case_study()


if __name__ == '__main__':
    main()
