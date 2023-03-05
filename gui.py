from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt

# Plot Lat/Lon Points from serial port
def plotLatLon(turtle_lat, turtle_lon, ship_lat, ship_lon):
    # Create points for Turtle that Geopandas can read from Lat/Lon pairs
    geometry_turtle = [Point(xy) for xy in zip(turtle_lat, turtle_lon)]
    gdf_turtle = GeoDataFrame(zip(turtle_lat, turtle_lon), geometry=geometry_turtle)

    # Create points for Ship that Geopandas can read from Lat/Lon pairs
    geometry_ship = [Point(xy) for xy in zip(ship_lat, ship_lon)]
    gdf_ship = GeoDataFrame(zip(ship_lat, ship_lon), geometry=geometry_ship)

    # And on the 3rd day of the hackathon, Bri created the world
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    ax = world.plot(figsize=(10, 6))

    # Plot Turtle and Ship coordinates on the world
    gdf_turtle.plot(ax=ax,  marker='o', color='red', markersize=15, label='turtle')
    gdf_ship.plot(ax=ax,  marker='o', color='purple', markersize=15, label='ship')

    # Set extent limits so plot is only on region of interest
    # XLim (West, East)
    # YLim (South, North)
    ax.set_xlim(-83.5, -77)
    ax.set_ylim(22, 28)

    # Set title, axis labels, legend
    plt.ion()
    plt.title("Squirtle Demo")
    plt.xlabel("Lat")
    plt.ylabel("Lon")
    plt.legend(loc="upper right")
    plt.show()
    plt.pause(1)
