import geopandas as gpd
import folium
import os

def plot_geospatial_data(file_path: str, data_dict: str, join_col_name: str, value_name: str, output_file_name: str):
    '''
    Function that plots geospatial information on the california map.
    
    Args:
        file_path (str): Path to the California shapefile (e.g., "tl_2020_us_state_500m.shp").
        data_dict (dict): Dictionary containing the geospatial data to plot. Eg. {zip_code: num_ev_cars}.
        join_col_name (str): Name of the column in the data_dict that matches the join column in the shapefile.
        value_name (str): Name of the column in the data_dict that contains the values to be plotted.
        output_file_name (str): Path to the output html file

    Returns:
        None
    '''
    
    assert isinstance(file_path, str) and isinstance(data_dict, dict) and isinstance(join_col_name, str) and isinstance(value_name, str)
    assert len(data_dict) > 0 and [isinstance(x, float) for x in list(data_dict.values())]
    assert os.path.exists(file_path)
    
    # Load California shapefile
    california_geojson = gpd.read_file(file_path).to_crs("EPSG:4326").to_json()
    california_center = [36.7783, -119.4179]
    california_map = folium.Map(location=california_center, zoom_start=6)

    # Plot data on the map using folium.Choropleth
    folium.Choropleth(
        geo_data=california_geojson,
        name='choropleth',
        data=data_dict,
        columns=[join_col_name, value_name],
        key_on=f'feature.properties.{join_col_name}',
        fill_color='YlGnBu',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=value_name
    ).add_to(california_map)

    # Save the map
    california_map.save(output_file_name)

    return

if __name__ == '__main__':
    file_path = 'California_Zip_Codes/California_Zip_Codes.shp'
    data_dict = {
                '92092': 100,
                '92037': 120,
                '92046': 140,
                }
    join_col_name = 'ZIP_CODE'
    value_name = 'Number of Cars'
    output_file_name = 'california_cars.html'
    plot_geospatial_data(file_path, data_dict, join_col_name, value_name, output_file_name)

