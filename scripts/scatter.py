import pandas as pd
import plotly.express as px

def scatter_plot(df: pd.DataFrame, x_col: str, y_col: str, xaxis_title: str, yaxis_title: str, title: str):
    '''
    Function that plots a scatter plots between 2 features of a dataset.
    
    Parameters:
        df  (pd.DataFrame): Pandas Dataframe
        x_col   (str): Feature of dataset to be plotted on x axis
        y_col   (str): Feature of dataset to be plotted on y axis
        xaxis_title (str): X axis label
        yaxis_title (str): Y axis label
        title   (str): Title of Plot
    Returns:
        None
    '''
    
    assert isinstance(df, pd.DataFrame) and isinstance(x_col, str) and isinstance(title, str)
    assert isinstance(y_col, str) and isinstance(xaxis_title, str) and isinstance(yaxis_title, str)
    assert x_col in list(df.columns) and y_col in list(df.columns)
    
    fig = px.scatter(df, x=x_col, y=y_col, trendline='ols')
    fig.update_layout(title=title,
                    xaxis_title=xaxis_title,
                    yaxis_title=yaxis_title)
    fig.show()
    fig.write_html(f'results/{title}.html')
