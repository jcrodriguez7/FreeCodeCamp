import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column

df['overweight'] = np.where(df['weight'] / ((df['height']/100)**2) > 25, 1, 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

df['cholesterol'].replace({1:0, 2:1,3:1},inplace=True)
df['gluc'].replace({1:0, 2:1,3:1},inplace=True)


# Draw Categorical Plot
def draw_cat_plot():

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df.melt(id_vars=['cardio'], value_vars=['active','alco', 'cholesterol','gluc','overweight','smoke'])


    # Draw the catplot with 'sns.catplot()'
    # Get the figure for the output
    fig = sns.catplot(data=df_cat, x="variable", hue="value", kind="count",col='cardio')


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo']<=df['ap_hi'])]
    df_heat = df_heat[df_heat['height'] >= df_heat['height'].quantile(0.025)]
    df_heat = df_heat[df_heat['height'] <= df_heat['height'].quantile(0.975)]
    df_heat = df_heat[df_heat['weight'] >= df_heat['weight'].quantile(0.025)]
    df_heat = df_heat[df_heat['weight'] <= df_heat['weight'].quantile(0.975)]

    # Calculate the correlation matrix
    corr = df_heat.corr()


    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True


    # Set up the matplotlib figure
    fig, ax = plt.subplots()


    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr,mask=mask,annot=True,fmt=".1f",linewidth=.5,ax=ax,vmin=-0.1, vmax=0.32)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

                   
                      
              
              
              
              
              
              
             