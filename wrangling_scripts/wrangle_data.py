import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """
    df = pd.read_csv('data/2019.csv')

    # first chart
    graph_one = []
    
    
    graph_one.append(
      go.Scatter(
      x = df['Score'],
      y = df['Healthy life expectancy'],
      mode = 'markers'
      )
    )
    
    layout_one = dict(title = 'Happiness vs. Healthy Life Expectancy',
                xaxis = dict(title = 'Happiness Score'),
                yaxis = dict(title = 'Healthy Life Expectancy'),
                )

    # second chart    
    graph_two = []
    
    graph_two.append(
      go.Scatter(
      x = df['Score'],
      y = df['Freedom to make life choices'],
      mode = 'markers'
      )
    )

    layout_two = dict(title = 'Happiness vs. Freedom of Life Choices',
                xaxis = dict(title = 'Happiness Score'),
                yaxis = dict(title = 'Freedom of Life Choices'),
                )


    # third chart
    graph_three = []
    graph_three.append(
      go.Scatter(
      x = df['Score'],
      y = df['Social support'],
      mode = 'markers'
      )
    )

    layout_three = dict(title = 'Happiness vs. Social Support',
                xaxis = dict(title = 'Happiness Score'),
                yaxis = dict(title = 'Social Support'),
                )
    
    # fourth chart
    graph_four = []
    
    graph_four.append(
      go.Scatter(
      x = df['Score'],
      y = df['GDP per capita'],
      mode = 'markers'
      )
    )

    layout_four = dict(title = 'Happiness vs. GDP',
                xaxis = dict(title = 'Happiness Score'),
                yaxis = dict(title = 'GDP per Capita'),
                )
    
    # fifth chart
    graph_five = []
    
    graph_five.append(
      go.Scatter(
      x = df['Score'],
      y = df['Generosity'],
      mode = 'markers'
      )
    )

    layout_five = dict(title = 'Happiness vs. Generosity',
                xaxis = dict(title = 'Happiness Score'),
                yaxis = dict(title = 'Generosity'),
                )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))
    figures.append(dict(data=graph_five, layout=layout_five))

    return figures