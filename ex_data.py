import random
import numpy as np
import matplotlib.pyplot as plt

def random_data(style="list", num_points=100, start=0, end=20, plot=False):

    if style == "list":
        # Return list of random numbers

        list = random.sample(range(start, end),num_points)
        return list
    
    elif style == "wave":
        # Return wave with random noise
        mean_noise = 0

        # num_points in time range start to end
        t = np.linspace(start, end, num_points)

        cycles = 3 # 3 cycles of the wave. Change if you wish.

        length = np.pi * 2 * cycles
        sin_wave = np.sin(np.arange(0, length, length/num_points))

        noise_scale = 0.3

        noise = np.random.normal(mean_noise, noise_scale, num_points)

        noisy_wave = sin_wave + noise

        if plot:
            # Plot signal with noise
            plt.figure()
            plt.plot(t, sin_wave, 'g') # clean sin wave is green
            plt.plot(t, noisy_wave, 'r') # messy wave is red
            plt.title('Signal with noise')
            plt.ylabel('Voltage (V)')
            plt.xlabel('Time (s)')
            plt.show()


        return noisy_wave


# random_data("wave", 200, 0, 50, False) # Plot with these qualities
        
            
