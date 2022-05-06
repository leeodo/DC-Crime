# Analyzing crime data and economic characteristics of wards in Washington, D.C.

# %%
# loading packages
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# %%
# loading data
crime_num_2020 = pd.read_csv("data/dc_violent_crimes.csv")
eco_characteristics = pd.read_csv("data/Economic Characteristics of DC Wards.csv")

# %%
# Merge the two datasets
merged_data = pd.merge(
    crime_num_2020, eco_characteristics, left_on="WARD", right_on="Ward"
)

# %%
# subset the data only will be graphed
statistics = merged_data[
    [
        "WARD",
        "violent_rate",
        "EMPLOYMENT STATUS: Civilian labor force: Unemployment Rate",
        "INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS): Total households: Mean household income (dollars)",
        "INCOME AND BENEFITS (IN 2019 INFLATION-ADJUSTED DOLLARS): Total households: Median household income (dollars)",
    ]
]
## rename the columns
statistics.columns = [
    "ward",
    "Crime Rate",
    "Unemployment Rate",
    "Mean Income",
    "Median Income",
]

# multiply the crime rate column by 100 to get the crime rate in percent and round to 1 decimal place
statistics["Crime Rate"] = statistics["Crime Rate"].apply(lambda x: round(x * 100, 3))

# make the data tidy
statistics = pd.melt(
    statistics, id_vars=["ward"], var_name="statistic", value_name="value"
)

## subset the data to two DFs for two graphs
stat_income = statistics.loc[
    (statistics["statistic"] == "Mean Income")
    | (statistics["statistic"] == "Median Income")
]

stat_percentages = statistics.loc[
    (statistics["statistic"] == "Crime Rate")
    | (statistics["statistic"] == "Unemployment Rate")
]

# %%
# graph mean and median income per wards
income_fig = px.bar(
    stat_income,
    x="ward",
    y="value",
    color="statistic",
    color_discrete_map={"Mean Income": "#fdd49e", "Median Income": "#ef6548"},
    barmode="group",
    title="Mean and Median Income per Ward",
    hover_name="statistic",
    hover_data={"statistic": False},
    labels={"value": "Dollars", "ward": "Ward", "statistic": "Statistic"},
)
income_fig.update_xaxes(type="category")
income_fig.write_html("html_viz/dc_income_fig.html")


# %%
# graph crime rate and unemployment rate per wards
percent_fig = px.bar(
    stat_percentages,
    x="ward",
    y="value",
    color="statistic",
    color_discrete_map={"Crime Rate": "#fdd49e", "Unemployment Rate": "#ef6548"},
    barmode="group",
    title="Crime Rate and Unemployment Rate per Ward",
    hover_name="statistic",
    hover_data={"statistic": False},
    labels={"value": "%", "ward": "Ward", "statistic": "Statistic"},
)
percent_fig.update_xaxes(type="category")
percent_fig.write_html("html_viz/dc_percent_fig.html")

# %%
