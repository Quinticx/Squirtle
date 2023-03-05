import pandas as pd
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt


# Read in CSV of Turtle locations
df_turtle = pd.read_csv("Squirtle - Turtle.csv", delimiter=',', skiprows=0, low_memory=False)
df_ship = pd.read_csv("Squirtle - Ship.csv", delimiter=',', skiprows=0, low_memory=False)

# Create points for Turtle that Geopandas can read from Lat/Lon pairs
geometry = [Point(xy) for xy in zip(df_turtle['Lat'], df_turtle['Lon'])]
gdf_turtle = GeoDataFrame(df_turtle, geometry=geometry)   

# Create points for Ship that Geopandas can read from Lat/Lon pairs
geometry = [Point(xy) for xy in zip(df_ship['Lat'], df_ship['Lon'])]
gdf_ship = GeoDataFrame(df_ship, geometry=geometry)   

# Plot points on the world
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
ax = world.plot(figsize=(10, 6))
gdf_turtle.plot(ax=ax,  marker='o', color='red', markersize=15, label='turtle')
gdf_ship.plot(ax=ax,  marker='o', color='purple', markersize=15, label='ship')

# Set extent limits so plot is only on region of interest
# XLim (West, East)
# YLim (South, North)
ax.set_xlim(-83.5, -77)
ax.set_ylim(22, 28)

# Set title, axis labels, legend
plt.title("Squirtle Demo")
plt.xlabel("Lat")
plt.ylabel("Lon")
plt.legend(loc="upper right")
plt.show()
