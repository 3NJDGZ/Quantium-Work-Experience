from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


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

# class TestApp(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.get("http://localhost:8050")
#
#     def tearDown(self):
#         self.driver.close()
#     def test_header_is_present(self):
#         header = self.driver.find_element(By.ID, "header")
#         self.assertIsNotNone(header)
#
#     def test_visualisation_is_present(self):
#         visualisation = self.driver.find_element(By.ID, "visualisation")
#         self.assertIsNotNone(visualisation)
#
#     def test_region_picker_is_present(self):
#         region_picker = self.driver.find_element(By.ID, "region-picker")
#         self.assertIsNotNone(region_picker)
#
# unittest.main()

app.run_server(debug=True)
