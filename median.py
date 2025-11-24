from ex_data import random_data
from plot_data import plot_data
import numpy as np
import statistics
import time


def median_filter(style="wave"):
    '''
    Use a random data list imitating filter output from 1 sensor
    Apply a median filter and print the results
    '''
    num_points = 100
    start = 0
    end = 20
    if style == "list":
        i = 0
        while i < 5:
            # Make a random data list 10 long
            data_list = random_data("list", 10)
            
            # Take the median of the data
            data_med = statistics.median(data_list)

            print("Random Data List:",data_list)
            print("Random Data Median: ",data_med,"\n")

            # Wait a short while (in seconds) then iterate
            time.sleep(0.5)
            i += 1
    elif style == "wave":
        i = 0
        point_list = []
        median_list = []
        noisy_wave = random_data("wave", num_points, start, end)
        for point in noisy_wave:
            point_list.append(point)
            if len(point_list) > 5:
                del point_list[0]
            
            # print(point_list)
            data_med = statistics.median(point_list)
            median_list.append(data_med)
            # print("median:",data_med)
            # print("cur median list: ",median_list)

        
        
        plot_data(num_points, noisy_wave, median_list)
        


            

    else:
        raise NameError("Invalid name of data style")

median_filter()