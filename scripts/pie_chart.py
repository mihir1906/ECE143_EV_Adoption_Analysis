import plotly.express as px

def plot_pie_chart(val: list, name: list, title: str):
	"""
	The following function plots a pie chart.

	Parameters:
		val (list): List of Values
		name (List): List of the labels 
		tite_str (str): Title for the plot

	Returns:
		None

	"""
	assert isinstance(val, list)
	assert isinstance(name, list)
	assert isinstance(title, str)

	fig = px.pie(values=val, names= name, title=title)
	fig.update_traces(textinfo='percent+label', hole=0.3)
	fig.show()
	fig.write_html(f'results/{title}.html')
