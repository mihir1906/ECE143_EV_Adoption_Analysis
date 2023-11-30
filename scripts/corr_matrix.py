import pandas as pd
import plotly.express as px

def plot_correlation_matrix(df: pd.DataFrame):
    '''
    Function that plots the pearson correlation matrix between given features of a dataframe
    
    Parameters:
        df  (pd.DataFrame): Pandas DataFrame with feature you want to plot pearson correlation
    Returns:
        None
    '''
    
    assert isinstance(df, pd.DataFrame)
    
    pearson_corr_matrix = df.corr()

    fig = px.imshow(
        pearson_corr_matrix,
        labels=dict(x="Features", y="Features", color="Correlation"),
        x=df.columns,
        y=df.columns,
        color_continuous_scale="YlOrRd",
        title="Correlation Matrix "
    )

    # Add annotations to display correlation values
    for i in range(len(df.columns)):
        for j in range(len(df.columns)):
            fig.add_annotation(
                x=df.columns[i],
                y=df.columns[j],
                text=f"{pearson_corr_matrix.iloc[j, i]:.2f}",
                showarrow=False,
                font=dict(color='black', size=12)
            )

    # Show the plot
    fig.show()
    fig.write_html(f'results/corr.html')