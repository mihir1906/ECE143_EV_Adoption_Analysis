def plot_pie_chart(val, name, title_str):
  """
     `Function Description:
     The following function plots a pie chart.
     
     `Parameters:
    - val (list): List of Values
    - name (List): List of the labels 
    - tite_str: Title for the plot

    `Returns:
    - None
    
    """
  assert isinstance(val, list)
  assert isinstance(val, list)
  assert isinstance(val, str)
  fig = px.pie(values=val, names= name, title=title_str)
  fig.update_traces(textinfo='percent+label', hole=0.3)
  fig.show()
