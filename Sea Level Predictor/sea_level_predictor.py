import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    
    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter( x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    
    

    # Create first line of best fit
    res = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    
    years = df['Year']._append(pd.Series(range(2014,2051)))
    
    plt.plot(years, res.intercept + res.slope*years, 'r', label='fitted line')

    # Create second line of best fit
    from2000 = df.loc[df['Year'] >= 2000]
    res_2 = linregress(x=from2000['Year'], y=from2000['CSIRO Adjusted Sea Level'])
    years_2 = from2000['Year']._append(pd.Series(range(2014,2051)))
    plt.plot(years_2, res_2.intercept + res_2.slope*years_2, 'r', label='fitted line')

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    # plt.show()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()