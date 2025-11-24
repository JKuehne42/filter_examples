import matplotlib.pyplot as plt
import numpy as np

def plot_data(num_points, start, end, dirty_data, clean_data, ylabel="Data Value", xlabel="point_number"):
    plt.figure()

    t = np.linspace(start, end, num_points)
    
    plt.plot(t, dirty_data, 'r', label = "Noisy") # messy wave is red
    plt.plot(t, clean_data, 'g', label = "filtered") # clean wave is green
    plt.title('Noisy and filtered wave')
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.legend()
    plt.show()