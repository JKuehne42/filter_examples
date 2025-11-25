from median import median_filter
from moving_average import average_filter
import argparse
import matplotlib.pyplot as plt
import numpy as np

def comp_filter():
    start = 0
    end = 20
    num_points = 100

    # Examine the other files to see how these functions work
    median_filter_result = median_filter("wave",False)
    average_filter_result = average_filter("wave",False)

    filtered_list = []
    alpha = 0.10

    t = np.linspace(start, end, num_points)     

    # This loop is to act as taking a new measurement at each time step.
    # The results are from the median and average filters respectively.
    for loop in t:
        med_point = median_filter_result[0]

        avg_point = average_filter_result[0]

        # Consider median 10% and average 90%
        filtered_value = alpha * med_point + (1 - alpha) * avg_point 

        filtered_list.append(filtered_value)

        del median_filter_result[0]
        del average_filter_result[0]

    plt.figure()


    length = np.pi * 2 * 3
    sin_wave = np.sin(np.arange(0, length, length/num_points))
    plt.plot(t, sin_wave, 'r', label = "No noise") # messy wave is red
    plt.plot(t, filtered_list, 'g', label = "Filtered") # clean wave is green
    plt.title('Noisy and filtered wave')
    plt.ylabel("Wave Output")
    plt.xlabel("Time")
    plt.legend()
    plt.show()


#TODO Run in your terminal using python complementary.py in the filters directory

if __name__ == "__main__":
    #### Define and parse (optional) arguments for the script ##
    parser = argparse.ArgumentParser(description='complementary filter')
    # parser.add_argument('--style',         default="wave",          type=str,           help='trajectory to plot (default: circle)', metavar='')
    ARGS = parser.parse_args()

    comp_filter(**vars(ARGS))



