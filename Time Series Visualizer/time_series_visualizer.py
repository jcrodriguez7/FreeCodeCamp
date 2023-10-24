import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",parse_dates=['date'],index_col='date')

# Clean data

df = df.loc[
    (df["value"] >= df["value"].quantile(0.025))
    & (df["value"] <= df["value"].quantile(0.975))
]

def draw_line_plot():
    # Draw line plot
    #draw plot 
    fig = plt.figure()
    plt.plot(df.index, df['value']) 
    plt.ylabel('Page Views')
    plt.xlabel('Date')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019') 

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():

    df_bar = df.copy(deep=True)
    df_bar["month"] = df.index.month
    df_bar["year"] = df.index.year
    df_bar = df_bar.groupby(["year", "month"])["value"].mean()

    df_bar = df_bar.unstack()

    fig = df_bar.plot(kind ="bar", legend = True, figsize = (8, 8)).figure
    plt.xlabel("Years", fontsize= 9)
    plt.ylabel("Average Page Views", fontsize= 9)
    plt.legend(fontsize = 10, labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():

    # Prepare data for box plots (this part is done!)
    df_box = df.copy(deep=True)
    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    df_box["month_1"] = df_box["date"].dt.month
    df_box = df_box.sort_values("month_1")

    fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2, figsize = (12,6))

    ax1.set_title("Year-wise Box Plot (Trend)")
    ax2.set_title("Month-wise Box Plot (Seasonality)")

    ax1.set_ylabel("Page Views")
    ax2.set_ylabel("Page Views")

    sns.boxplot(x=df_box["Year"], y=df_box["value"], ax = ax1)
    sns.boxplot(x=df_box["Month"], y=df_box["value"], ax = ax2)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
