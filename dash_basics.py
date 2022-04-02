# for data storage
import pandas as pd
# display charts
import plotly.express as px
import plotly.graph_objects as go
# render to website
import dash
import dash_html_components as html
import dash_core_components as dcc

# Read the airline data into pandas dataframe
airline_data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv',
                           encoding="ISO-8859-1",
                           dtype={'Div1Airport': str, 'Div1TailNum': str,
                                  'Div2Airport': str, 'Div2TailNum': str})


# Randomly sample 500 data points. Setting the random state to be 42 so that we get same result.
data = airline_data.sample(n=500, random_state=42)

# Pie Chart Creation
fig = px.pie(data, values='Flights', names='DistanceGroup',
             title='Distance group proportion by flights')

fig2 = go.Figure(data=go.Scatter(
    x=data['OriginStateName'], y=data['Year'], mode='markers', marker=dict(color='red')))

fig2.update_layout(title='Origin', xaxis_title='States', yaxis_title='Year')

line_data = data.groupby('Month')['ArrDelay'].mean().reset_index()
fig3 = go.Figure(data=go.Scatter(
    x=line_data['Month'], y=line_data['ArrDelay']))
fig3.update_layout(title='average delay ',
                   xaxis_title='months', yaxis_title='delay ')
                   
# Create a dash application
app = dash.Dash(__name__)

# Get the layout of the application and adjust it.
# Create an outer division using html.Div and add title to the dashboard using html.H1 component
# Add description about the graph using HTML P (paragraph) component
# Finally, add graph component.
app.layout = html.Div(children=[html.H1('Airline Dashboard', style={'textAlign': 'center', 'color': '#503D36', 'font-size': 70}),
                                html.P('Pie chart', style={
                                    'textAlign': 'center', 'color': '#F57241'}),
                                # display the pie created by plotly
                                dcc.Graph(figure=fig),

                                html.P("Scattered plot", style={
                                       'textAlign': 'center', 'color': '#F57241'}),
                                dcc.Graph(figure=fig2),

                                html.P("Line chart", style={
                                       'textAlign': 'center', 'color': '#F57241'}),
                                dcc.Graph(figure=fig3)
                                ])

# Run the application
if __name__ == '__main__':
    app.run_server()
