from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

app = Dash(__name__)

app.layout = html.Div([
    html.H4("Pink Morsel Sales per Regions"),
    dcc.Graph(id="graph"),
    dcc.Checklist(
        id="checklist",
        options=["north", "east", "south", "west"],
        inline=True
    ),
])

@app.callback(
    Output("graph", "figure"), 
    Input("checklist", "value"))
def update_line_chart(regions):
    df = pd.read_csv("dataprocessed.csv") # replace with your own data source
    mask = df.region.isin(regions)
    fig = px.line(df[mask], 
        x="date", y="sales", color='region')
    return fig


app.run_server(debug=True)