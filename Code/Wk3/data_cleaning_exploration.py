# pip install geopandas matplotlib plotly 

import pandas as pd 
import geopandas as gpd
import json


df = pd.read_csv('Code/Wk3/data/PLACES__Local_Data_for_Better_Health__Census_Tract_Data_2023_release_20240403.csv')

ny = df[df['StateAbbr'] == 'NY']
len(ny)

ny.to_csv('Code/Wk3/data/ny_places2023.csv', index=False)

## get first 1000 rows
ny_small = ny.head(1000)
ny_small.to_csv('Code/Wk3/data/ny_places2023_small.csv', index=False)

ny.head()







####### TESTING 


# Load small 
ny_small = pd.read_csv('Code/Wk3/data/ny_places2023.csv')

# Load the shapefile
gdf = gpd.read_file('Code/Wk3/data/tl_2021_36_tract.shp')
print(gdf.head())
print(gdf.columns)
gdf.GEOID
## get type of variable GEOID is
gdf.GEOID.dtype
gdf.GEOID = gdf.GEOID.astype('int64')


# Assuming df is your census data DataFrame
ny_small['Geolocation'] = gpd.GeoSeries.from_wkt(ny_small['Geolocation'])
ny_small['GEOID'] = ny_small['LocationID']

# Convert df to a GeoDataFrame
gdf_data = gpd.GeoDataFrame(ny_small, geometry='Geolocation')

# Merge with the shapefile GeoDataFrame based on a common column, e.g., 'LocationID'
merged_gdf = gdf.merge(gdf_data, on='GEOID', how='inner')

## save merged_gdf as csv 
# merged_gdf.to_csv('Code/Wk3/data/merged_small_gdf.csv', index=False)



## Create simple visualizaiton example 

filtered_gdf = merged_gdf[(merged_gdf['Measure'] == 'Obesity among adults aged >=18 years') &
                   (merged_gdf['Data_Value_Type'] == 'Crude prevalence')]

## keep only unique rows with a unique LocationID
outline = merged_gdf.drop_duplicates(subset='LocationID')
outline.plot("filtered_gdf", legend=False, figsize=(25, 25)) 








geojson = filtered_gdf.__geo_interface__

# Create an interactive map using Plotly Express
fig = px.choropleth_mapbox(filtered_gdf,
                           geojson=geojson,
                           locations=filtered_gdf.index,
                           color="Data_Value",
                           color_continuous_scale="OrRd",
                           range_color=(filtered_gdf["Data_Value"].min(), filtered_gdf["Data_Value"].max()),
                           mapbox_style="carto-positron",
                           zoom=5,
                           center={"lat": filtered_gdf.geometry.centroid.y.mean(), 
                                   "lon": filtered_gdf.geometry.centroid.x.mean()},
                           opacity=0.5,
                           labels={"Data_Value": "Obesity Prevalence (%)"})
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},
                  title_text="Obesity Prevalence in New York State by Census Block")
fig.show()