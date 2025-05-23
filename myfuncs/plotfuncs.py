import myfuncs.myfuncs as mf

import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, MonthLocator

import seaborn as sns

def preprocess_chart_data(df, x_col, y_col):
    """
    Preprocess the data for plotting: clean labels, sort data, and ensure numeric columns.
    """
    x_label = mf.clean_label(x_col)
    y_label = mf.clean_label(y_col)

    # Convert x_col to datetime for sort3ing
    df['x_col'] = pd.to_datetime(df[x_col], errors='coerce')
    df = df.set_index('x_col').sort_index()

    # Ensure numeric columns
    df = df.apply(pd.to_numeric, errors='coerce')
    # sorted_columns = df.sum().sort_values(ascending=False).index
    # df_sorted = df[sorted_columns]

    return df, x_label, y_label

def setup_plot(l, h, title, x_label, y_label, **kwargs):
    """
    Set up the plot with titles, labels, and axis limits.
    """
    sns.set(style="whitegrid")
    plt.figure(figsize=(l, h))
    ax = plt.gca()

    plt.title(title, fontsize=20)
    plt.xlabel(x_label, fontsize=16)
    plt.ylabel(y_label, fontsize=16)
    plt.tight_layout()

    # Set limits
    if kwargs.get():
        ax.set_xlim(x_limits)
    if y_limits:
        ax.set_ylim(y_limits)

    # Set x-ticks
    if x_ticks == 'monthly':
        ax.xaxis.set_major_locator(MonthLocator())
        ax.xaxis.set_major_formatter(DateFormatter('%b %Y'))
        plt.xticks(rotation=45, ha='right', fontsize=13)

    # Set y-ticks
    if y_ticks:
        ax.set_yticks(y_ticks)

    plt.legend(title=y_label, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()



def plot_line_chart(df, x_col, y_col, l=10, h=6, title='Line Chart', **kwargs):
    x_limits = kwargs.get('x_limits',False)
    y_limits = kwargs.get('y_limits',False)
    x_ticks = kwargs.get('x_ticks',False)
    y_ticks = kwargs.get('y_ticks',False)

    df, x_label, y_label = preprocess_chart_data(df, x_col, y_col)

    # Plot line chart
    for col in df.columns:
        sns.lineplot(data=df, x=df.index, y=col, marker='o', label=mf.clean_label(col))

    df.plot(kind='bar', stacked=True, ax=plt.gca())
    df.plot(kind='bar', stacked=False, ax=plt.gca())

    setup_plot(
        l, h, title, x_label, y_label,
        x_limits=x_limits, y_limits=y_limits,
        x_ticks=x_ticks, y_ticks=y_ticks
    )


def plot_stacked_bar_chart(df, x_col, y_col, l=10, h=6, title='Stacked Bar Chart', **kwargs):
    x_limits = kwargs.get('x_limits',False)
    y_limits = kwargs.get('y_limits',False)
    x_ticks = kwargs.get('x_ticks',False)
    y_ticks = kwargs.get('y_ticks',False)

    df, x_label, y_label = preprocess_chart_data(df, x_col, y_col)

    # Plot stacked bar chart
    df.plot(kind='bar', stacked=True, ax=plt.gca())

    setup_plot(
        l, h, title, x_label, y_label,
        x_limits=x_limits, y_limits=y_limits,
        x_ticks=x_ticks, y_ticks=y_ticks
    )

def plot_clustered_bar_chart(df, x_col, y_col, l=10, h=6, title='Clustered Bar Chart', **kwargs):
    x_limits = kwargs.get('x_limits',False)
    y_limits = kwargs.get('y_limits',False)
    x_ticks = kwargs.get('x_ticks',False)
    y_ticks = kwargs.get('y_ticks',False)

    df, x_label, y_label = preprocess_chart_data(df, x_col, y_col)

    # Plot clustered bar chart
    df.plot(kind='bar', stacked=False, ax=plt.gca())

    setup_plot(
        l, h, title, x_label, y_label,
        x_limits=x_limits, y_limits=y_limits,
        x_ticks=x_ticks, y_ticks=y_ticks
    )