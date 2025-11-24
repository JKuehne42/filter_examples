from ex_data import random_data
from plot_data import plot_data
import statistics
import time
import argparse


def average_filter(style="wave", plot=True):
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
            data_avg = sum(data_list)/len(data_list)

            print("Random Data List:",data_list)
            print("Random Data Median: ",data_avg,"\n")

            # Wait a short while (in seconds) then iterate
            time.sleep(0.5)
            i += 1
        return data_avg

    elif style == "wave":
        i = 0
        point_list = []
        avg_list = []
        noisy_wave = random_data("wave", num_points, start, end)
        for point in noisy_wave:
            point_list.append(point)
            if len(point_list) > 5:
                del point_list[0]
            
            data_avg = sum(point_list)/len(point_list)
            avg_list.append(data_avg)
        
        if plot:
            plot_data(num_points, start, end, noisy_wave, avg_list)
        
        return avg_list
    
    else:
        raise NameError("Invalid name of data style")

if __name__ == "__main__":
    #### Define and parse (optional) arguments for the script ##
    parser = argparse.ArgumentParser(description='moving average filter')
    parser.add_argument('--style',         default="wave",          type=str,           help='trajectory to plot (default: circle)', metavar='')
    ARGS = parser.parse_args()

    average_filter(**vars(ARGS))