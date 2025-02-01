 import dash
 from dash import dcc, html
 import plotly.express as px
 import pandas as pd
 app = dash.Dash(__name__)
 # Load your log data
 df = pd.read_csv('synthetic_logs.log', sep=':', header=None)
 df.columns = ['Level', 'Message','Text','Display']
 # Create a plot
 fig = px.histogram(df, x='Level')
 app.layout = html.Div(children=[html.H1(children='Log Data Visualization'),
 dcc.Graph( id='log-level-histogram', figure=fig)])
 01 - BRANDING
 if __name__ == '__main__':
 app.run_server(debug=True)
