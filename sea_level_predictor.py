import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    fig, ax = plt.subplots(1,1)
    ax.scatter(df.Year, df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df.Year, df['CSIRO Adjusted Sea Level'])

    years_extended = np.arange(1880, 2050, 1)

    ax.plot(years_extended, intercept + slope*years_extended, 'r', label='fitted line')
    ax.set_xlim(1850, 2075)


    # Create second line of best fit
    recent_years = np.arange(2000, 2014, 1)
    recent_data = df['CSIRO Adjusted Sea Level'][df.Year >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(recent_years, recent_data)

    years_extended2 = np.arange(2000, 2050, 1)

    ax.plot(years_extended2, intercept2 + slope2*years_extended2, 'g', label='fitted line')


    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()