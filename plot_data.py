import matplotlib.pyplot as plt

def plot_data(num_points, dirty_data, clean_data, ylabel="Data Value", xlabel="point_number"):
    plt.figure()
    plt.plot(num_points, dirty_data, 'r') # messy wave is red
    plt.plot(num_points, clean_data, 'g') # clean wave is green
    plt.title('Signal with noise')
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.show()