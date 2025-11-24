from median import median_filter
from moving_average import average_filter
import argparse
import matplotlib.pyplot as plt
import numpy as np

def comp_filter():
    start = 0
    end = 20
    num_points = 100
    median_filter_result = median_filter("wave",False)
    average_filter_result = average_filter("wave",False)
    # print(average_filter_result)
    print(median_filter_result)

    # Iterate through these to produce a better result

    filtered_list = []

    k_med = 0.60
    k_avg = 0.40

    while len(median_filter_result) + len(average_filter_result) > 0:
        med_point = median_filter_result[0]
        avg_point = average_filter_result[0]

        filtered_list.append(med_point*k_med+avg_point*k_avg)

        del median_filter_result[0]
        del average_filter_result[0]


    plt.figure()

    t = np.linspace(start, end, num_points)     

    length = np.pi * 2 * 3
    sin_wave = np.sin(np.arange(0, length, length/num_points))
    plt.plot(t, sin_wave, 'r', label = "No noise") # messy wave is red
    plt.plot(t, filtered_list, 'g', label = "Filtered") # clean wave is green
    plt.title('Noisy and filtered wave')
    plt.ylabel("Wave Output")
    plt.xlabel("Time")
    plt.legend()
    plt.show()








if __name__ == "__main__":
    #### Define and parse (optional) arguments for the script ##
    parser = argparse.ArgumentParser(description='complementary filter')
    # parser.add_argument('--style',         default="wave",          type=str,           help='trajectory to plot (default: circle)', metavar='')
    ARGS = parser.parse_args()

    comp_filter(**vars(ARGS))



