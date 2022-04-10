# Wrangling data for DC crime data

# %%
# import packages
import pandas as pd

# %%
# read in data
df = pd.read_csv("data/dc.csv")

# %%
# Getting total number of crimes per day
df["START_DATE"] = pd.to_datetime(df["START_DATE"]).dt.date
df["END_DATE"] = pd.to_datetime(df["END_DATE"]).dt.date
df["REPORT_DAT"] = pd.to_datetime(df["REPORT_DAT"]).dt.date

# %%
# create a new DataFrame with number of crimes per day
num_crimes = df.groupby("REPORT_DAT").size()
num_crimes = pd.DataFrame(
    {"REPORT_DAT": num_crimes.index, "num_crimes": num_crimes.values}
)

num_crimes.to_csv("data/num_crimes.csv", index=False)

# create a new DataFrame with number of individual crimes types per day
num_crimes_type = df.groupby(["REPORT_DAT", "offense-text"]).size()
num_crimes_type = pd.DataFrame(
    {
        "REPORT_DAT": num_crimes_type.index.get_level_values(0),
        "offense-text": num_crimes_type.index.get_level_values(1),
        "num_crimes_type": num_crimes_type.values,
    }
)

num_crimes_type.to_csv("data/num_crimes_type.csv", index=False)

# create a new DataFrame with number of crimes per day per Ward
num_crimes_ward = df.groupby(["REPORT_DAT", "WARD"]).size()
num_crimes_ward = pd.DataFrame(
    {
        "REPORT_DAT": num_crimes_ward.index.get_level_values(0),
        "WARD": num_crimes_ward.index.get_level_values(1),
        "num_crimes_ward": num_crimes_ward.values,
    }
)

num_crimes_ward.to_csv("data/num_crimes_ward.csv", index=False)

# create a new DataFrame with number of crimes per day per Ward and crime type
num_crimes_ward_type = df.groupby(["REPORT_DAT", "WARD", "offense-text"]).size()
num_crimes_ward_type = pd.DataFrame(
    {
        "REPORT_DAT": num_crimes_ward_type.index.get_level_values(0),
        "WARD": num_crimes_ward_type.index.get_level_values(1),
        "offense-text": num_crimes_ward_type.index.get_level_values(2),
        "num_crimes_ward_type": num_crimes_ward_type.values,
    }
)

num_crimes_ward_type.to_csv("data/num_crimes_ward_type.csv", index=False)
