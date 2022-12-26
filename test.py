import dash
from dash import dcc
from dash import html
from plotly import graph_objs as go

import pandas as pd

df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y1': [1, 4, 9, 16, 25],
    'y2': [2, 8, 18, 32, 50],
    'group': ['A', 'A', 'A', 'B', 'B']
})
def create_figure(df):
    traces = []
    groups = df['group'].unique()
    for group in groups:
        df_group = df[df['group'] == group]
        traces.append(go.Scatter(
            x=df_group['x'],
            y=df_group['y1'],
            name=f'y1 ({group})'
        ))
        traces.append(go.Scatter(
            x=df_group['x'],
            y=df_group['y2'],
            name=f'y2 ({group})'
        ))
    return go.Figure(data=traces)
app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(id='line-graph', figure=create_figure(df))
])
app.run_server()