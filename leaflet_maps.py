# Building interactive maps with Leaflet

# %%
import folium
import pandas as pd
import geopandas as gpd

# %%
# read in data
df = pd.read_csv("data/dc_num_crimes_ward_2021.csv")
dc_gpd = gpd.read_file("Wards_from_2012.geojson")

# %%
# Merge the two dataframes
gdf = dc_gpd.merge(df, on="WARD", how="left").fillna(0)

# %%
# create a map
map = folium.Map(location=[38.9072, -77.0369], zoom_start=11)


# %%
# bind geojson data to map
colormap = folium.LinearColormap(
    colors=["red", "orange", "yellow", "green"],
    vmin=gdf.loc[gdf["num_crimes_ward_2021"] > 0, "num_crimes_ward_2021"].min(),
    vmax=gdf.loc[gdf["num_crimes_ward_2021"] > 0, "num_crimes_ward_2021"].max(),
).to_step(n=5)

folium.GeoJson(
    gdf[["geometry", "WARD", "num_crimes_ward_2021"]],
    name="DC Crime Map 2021",
    style_function=lambda x: {
        "weight": 2,
        "color": "black",
        "fillColor": colormap(x["properties"]["num_crimes_ward_2021"]),
        "fillOpacity": 0.2,
    },
    highlight_function=lambda x: {"weight": 3, "color": "black"},
    smooth_factor=0.1,
    tooltip=folium.features.GeoJsonTooltip(
        fields=[
            "WARD",
            "num_crimes_ward_2021",
        ],
        aliases=["WARD", "Total Crimes 2021"],
        labels=True,
        sticky=True,
        toLocaleString=True,
    ),
).add_to(map)

colormap.add_to(map)

map

# %%
# saving the map
map.save("dc_crime_map_2021.html")

# %%
