import dash
import csv
import pandas as pd 
from dash import dcc
from dash import html
import plotly.express as px

# Load the data
df = pd.read_csv('dataprocessed.csv')
print(df.head())

# Create the Dash app
app = dash.Dash()

# Define the layout of the app
app.layout = html.Div([
  # Add the line chart
  dcc.Graph(
    id='line-chart',
    figure={
      'data': [
        {'x': df['date'], 'y': df['sales'], 'type': 'line', 'name': 'Total Sales'}
      ],
      'layout': {
        'title': 'Sales Generated Over Time'
      }
    }
  )
])

# Run the app
if __name__ == '__main__':
  app.run_server(debug=True)
