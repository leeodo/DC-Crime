import pandas as pd
import glob
import os
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = "browser"
pio.templates.default = "plotly_white"


path1 = r"A5/eco/sm/04_sm_csv"
path2 = r"A5/eco/sm/05_sm_csv"
path3 = r"A5/eco/sm/06_sm_csv"


content1 = []
content2 = []
content3 = []

for myfile in glob.glob(path1 + "/*.csv"):
    tmp = pd.read_csv(myfile, index_col=None, na_values="-1", header=None).iloc[:, 0:1]
    date = myfile[-14:-4]
    df2 = pd.DataFrame()
    df2["sum"] = tmp[0].sum()
    df2.loc[0] = tmp[0].sum()
    df2["date"] = date
    content1.append(df2)

df4 = pd.concat(content1)


for myfile in glob.glob(path2 + "/*.csv"):
    tmp = pd.read_csv(myfile, index_col=None, na_values="-1", header=None).iloc[:, 0:1]
    date = myfile[-14:-4]
    df2 = pd.DataFrame()
    df2["sum"] = tmp[0].sum()
    df2.loc[0] = tmp[0].sum()
    df2["date"] = date
    content2.append(df2)

df5 = pd.concat(content2)


for myfile in glob.glob(path3 + "/*.csv"):
    tmp = pd.read_csv(myfile, index_col=None, na_values="-1", header=None).iloc[:, 0:1]
    date = myfile[-14:-4]
    df2 = pd.DataFrame()
    df2["sum"] = tmp[0].sum()
    df2.loc[0] = tmp[0].sum()
    df2["date"] = date
    content3.append(df2)

df6 = pd.concat(content3)


df4 = df4.sort_values(by=["date"])
df5 = df5.sort_values(by=["date"])
df6 = df6.sort_values(by=["date"])

df4["household"] = 4
df5["household"] = 5
df6["household"] = 6

df = pd.concat([df4, df5, df6])


## Vis


household4 = go.Scatter(
    x=df4["date"][:2],
    y=df4["sum"][:2],
    mode="lines",
    line=dict(width=1.5),
    name="household 4",
)
household5 = go.Scatter(
    x=df5["date"][:2],
    y=df5["sum"][:2],
    mode="lines",
    line=dict(width=1.5),
    name="household 5",
)
household6 = go.Scatter(
    x=df6["date"][:2],
    y=df6["sum"][:2],
    mode="lines",
    line=dict(width=1.5),
    name="household 6",
)

frames = [
    dict(
        data=[
            dict(type="scatter", x=df4["date"][: k + 1], y=df4["sum"][: k + 1]),
            dict(type="scatter", x=df5["date"][: k + 1], y=df5["sum"][: k + 1]),
            dict(type="scatter", x=df6["date"][: k + 1], y=df6["sum"][: k + 1]),
        ],
        traces=[0, 1, 2],
    )
    for k in range(1, len(df4) - 1)
]

layout = go.Layout(
    width=1500,
    height=800,
    showlegend=False,
    hovermode="x unified",
    updatemenus=[
        dict(
            type="buttons",
            showactive=False,
            y=1.05,
            x=1.15,
            xanchor="right",
            yanchor="top",
            pad=dict(t=0, r=10),
            buttons=[
                dict(
                    label="Play",
                    method="animate",
                    args=[
                        None,
                        dict(
                            frame=dict(duration=3, redraw=False),
                            transition=dict(duration=0),
                            fromcurrent=True,
                            mode="immediate",
                        ),
                    ],
                )
            ],
        ),
        dict(
            type="buttons",
            direction="left",
            buttons=list(
                [
                    dict(
                        args=[{"yaxis.type": "linear"}],
                        label="LINEAR",
                        method="relayout",
                    ),
                    dict(args=[{"yaxis.type": "log"}], label="LOG", method="relayout"),
                ]
            ),
        ),
    ],
)
layout.update(
    xaxis=dict(range=["2012-06-20", "2013-02-1"], autorange=False),
    yaxis=dict(range=[0, 230000000], autorange=False),
)

fig = go.Figure(data=[household4, household5, household6], frames=frames, layout=layout)

fig.update_layout(
    {
        "title": "Real Power Over All Power Phases Consumed in Three Selected Household<br><sup>Source: the Electricity Consumption and Occupancy (ECO) data set</sup>",
        "xaxis": {"title": "Time"},
        "yaxis": {"title": "Total real power consumed (Watt)"},
        "legend": {"title": "Households"},
        "showlegend": True,
    }
)


fig.show()

fig.write_html("plotly.html")
