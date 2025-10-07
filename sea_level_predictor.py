import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import io

def draw_plot():
    # Step 1: Read data

    df = pd.read_csv('epa-sea-level.csv', na_values='null') 

    df_cleaned = df.dropna(subset=['CSIRO Adjusted Sea Level'])

    # Step 2: Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df_cleaned['Year'], df_cleaned['CSIRO Adjusted Sea Level'], label='Original Data')

    # Step 3: Create first line of best fit
    res_all = linregress(df_cleaned['Year'], df_cleaned['CSIRO Adjusted Sea Level'])
    x_pred_all = pd.Series(range(df_cleaned['Year'].min(), 2051))
    y_pred_all = res_all.slope * x_pred_all + res_all.intercept
    ax.plot(x_pred_all, y_pred_all, 'r', label='Best Fit (All Data)')

    # Step 4: Create second line of best fit
    df_recent = df_cleaned[df_cleaned['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred_recent = pd.Series(range(2000, 2051))
    y_pred_recent = res_recent.slope * x_pred_recent + res_recent.intercept
    ax.plot(x_pred_recent, y_pred_recent, 'g', label='Best Fit (Since 2000)')

    # Step 5: Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    
    # Save plot and return data for testing 
    plt.savefig('sea_level_plot.png')

    return plt.gca()
