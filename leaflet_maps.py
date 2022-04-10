# Building interactive maps with Leaflet

# %%
import folium
import pandas as pd
import geopandas as gpd
import datetime

datetime.datetime.strptime

# %%
# read in data
df = pd.read_csv("data/dc_num_crimes_ward_2021.csv")
df1 = pd.read_csv("data/dc_num_crimes_ward_type.csv")
dc_gpd = gpd.read_file("Wards_from_2012.geojson")

# %%
# Merge the two dataframes
gdf = dc_gpd.merge(df, on="WARD", how="left").fillna(0)
gdf["crime_rate"] = gdf["num_crimes_ward_2021"] / gdf["POP_2011_2015"]

# %%
# Mugleing the df1 for 2021 crime type summary
df1["REPORT_DAT"] = pd.to_datetime(df1["REPORT_DAT"]).dt.date
df1 = df1[
    (df1["REPORT_DAT"] >= datetime.date(2021, 1, 1))
    & (df1["REPORT_DAT"] <= datetime.date(2021, 12, 31))
]
df1 = df1.groupby(["WARD", "offense-text"]).sum().reset_index()

df1["WARD"] = df1["WARD"].astype(int)

dc_robbery = df1[df1["offense-text"] == "robbery"][
    ["WARD", "num_crimes_ward_type"]
].reindex()
dc_robbery = dc_robbery.rename(columns={"num_crimes_ward_type": "robbery"})
dc_sex_abuse = df1[df1["offense-text"] == "sex abuse"][
    ["WARD", "num_crimes_ward_type"]
].reindex()
dc_sex_abuse = dc_sex_abuse.rename(columns={"num_crimes_ward_type": "sex_abuse"})

gdf1 = dc_gpd.merge(dc_robbery, on="WARD", how="left").fillna(0)
gdf1 = gdf1.merge(dc_sex_abuse, on="WARD", how="left").fillna(0)

# %%
# create a map
map = folium.Map(location=[38.9072, -77.0369], zoom_start=11)


# %%
# bind geojson data to map
variable = "num_crimes_ward_2021"

colormap = folium.LinearColormap(
    colors=[(230, 230, 250), (75, 0, 130)],
    vmin=gdf.loc[gdf[variable] > 0, variable].min(),
    vmax=gdf.loc[gdf[variable] > 0, variable].max(),
)

folium.GeoJson(
    gdf[["geometry", "WARD", variable, "crime_rate"]],
    name="DC Crime Map 2021",
    style_function=lambda x: {
        "weight": 2,
        "color": "black",
        "fillColor": colormap(x["properties"][variable]),
        "fillOpacity": 0.5,
    },
    highlight_function=lambda x: {"weight": 3, "color": "black"},
    smooth_factor=0.1,
    tooltip=folium.features.GeoJsonTooltip(
        fields=[
            "WARD",
            variable,
            "crime_rate",
        ],
        aliases=["WARD", "Total Crimes 2021", "Crime Rate 2021"],
        labels=True,
        sticky=True,
        toLocaleString=True,
    ),
).add_to(map)

colormap.add_to(map)

# %%
# saving the map
map.save("dc_crime_map_2021.html")

# %%
# map with crime types
map1 = gdf1.explore(
    column="robbery",  # column to explode
    tooltip="robbery",
    scheme="naturalbreaks",  # use mapclassify's natural breaks scheme
    legend=True,  # show legend
    k=10,  # use 10 bins
    legend_kwds=dict(colorbar=False),  # do not use colorbar
    name="Robbery",  # name of the layer in the map
)

gdf1.explore(
    m=map1, column="sex_abuse", tooltip=["sex_abuse", "robbery"], name="Sex Abuse"
)

folium.TileLayer("Stamen Toner", control=True).add_to(
    map1
)  # use folium to add alternative tiles
folium.LayerControl().add_to(map1)  # use folium to add layer control

map1.save("dc_rob_sex_crime_2021.html")

# %%
