import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_bar_scatter(scatter: dict, bar: dict, y_labels: list, annots: list, title: str):
    '''
    Function to plot a joint bar and scatter plot. The left graph will be a bar plot show distribution of data. 
    The right graph will be a scatter plot.
    
    Parameters:
        scatter (dict): Data for scatter plot. {"data": [], "name":str}
        bar (dict): Data for bar plots. {"column_name": data}
        y_labels    (list): Valuess on Y-axis. i.e name of city, ZIP etc.
        annots  (list): Annotation values for scatter plot.
        title   (str): Title of the plot.
    Returns:
        None
    '''
    
    fig = make_subplots(rows=1, cols=2, specs=[[{}, {}]], shared_xaxes=True, shared_yaxes=False, vertical_spacing=0.1)
    
    
    fig.append_trace(go.Scatter(
        x=scatter['data'], 
        y=y_labels,
        mode='lines+markers',
        name=scatter['name'],
    ), 1, 2)
    
    for k, v in bar.items():
        fig.add_trace(go.Bar(
            x=v,  
            y=y_labels,    
            name=k,
            orientation='h',
        ));
    
    fig.update_layout(
        title=f'Fuel Type distribution for {title}',
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=True,
            domain=[0, 0.85],
        ),
        yaxis2=dict(
            showgrid=False,
            showline=True,
            showticklabels=False,
            linecolor='rgba(102, 102, 102, 0.8)',
            linewidth=2,
            domain=[0, 0.85],
        ),
        xaxis=dict(
            zeroline=False,
            showline=False,
            showticklabels=True,
            showgrid=True,
            domain=[0, 0.42],
        ),
        xaxis2=dict(
            zeroline=True,
            showline=True,
            showticklabels=True,
            showgrid=True,
            domain=[0.47, 1],
            side='top',
            dtick=25000,
            autorange='reversed'
        ),
        legend=dict(x=10, y=1.038, font_size=10),
        margin=dict(l=100, r=20, t=70, b=70),
        paper_bgcolor='rgb(248, 248, 255)',
        plot_bgcolor='rgb(248, 248, 255)',
        barmode='relative'
    );
    
    annotations = []
    ev_round = np.round(annots, decimals=2)
    for ydn, xd in zip(ev_round, y_labels):
        annotations.append(dict(xref='x2', yref='y2',
                                y=xd, x=ydn+0.6 ,
                                text='{:,}'.format(ydn) + '%',
                                font=dict(family='Times New Roman', size=12,
                                        color='rgb(120, 90, 109)'),
                                showarrow=False))
    
    fig.update_layout(annotations=annotations)
    fig.show()
    fig.write_html(f'results/{title}.html')