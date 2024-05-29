import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('abnormal_data.csv')
past_df = pd.read_csv('past_data.csv')

df['vibration'] = (df['accX']**2 + df['accY']**2 + df['accZ']**2)**0.5
past_df['vibration'] = (past_df['accX']**2 + past_df['accY']**2 + past_df['accZ']**2)**0.5

app = dash.Dash(__name__)

colors = {
    'background': '#EAEAEA',
    'text': '#0a2540',
    'plot_background': '#FFFFFF',
    'grid': '#d9d9d9',
    'turquoise': '#003E3F',
    'black': '#2C0703',
}

fig_temp = px.line(title='Real Time Temperature', color_discrete_sequence=[colors['black']])
fig_temp.update_layout(
    plot_bgcolor=colors['plot_background'],
    paper_bgcolor=colors['background'],
    font_color=colors['black'],
    title_font=dict(size=24, family='Arial Black, sans-serif', color=colors['turquoise']),
    xaxis=dict(showgrid=True, gridcolor=colors['grid']),
    yaxis=dict(showgrid=True, gridcolor=colors['grid'])
)

fig_voltage = px.line(title='Real Time Voltage', color_discrete_sequence=[colors['black']])
fig_voltage.update_layout(
    plot_bgcolor=colors['plot_background'],
    paper_bgcolor=colors['background'],
    font_color=colors['black'],
    title_font=dict(size=24, family='Arial Black, sans-serif', color=colors['turquoise']),
    xaxis=dict(showgrid=True, gridcolor=colors['grid']),
    yaxis=dict(showgrid=True, gridcolor=colors['grid'])
)

fig_light = px.line(title='Real Time Light Level', color_discrete_sequence=[colors['black']])
fig_light.update_layout(
    plot_bgcolor=colors['plot_background'],
    paper_bgcolor=colors['background'],
    font_color=colors['black'],
    title_font=dict(size=24, family='Arial Black, sans-serif', color=colors['turquoise']),
    xaxis=dict(showgrid=True, gridcolor=colors['grid']),
    yaxis=dict(showgrid=True, gridcolor=colors['grid'])
)

fig_vibration = px.line(title='Real Time Vibration', color_discrete_sequence=[colors['black']])
fig_vibration.update_layout(
    plot_bgcolor=colors['plot_background'],
    paper_bgcolor=colors['background'],
    font_color=colors['black'],
    title_font=dict(size=24, family='Arial Black, sans-serif', color=colors['turquoise']),
    xaxis=dict(showgrid=True, gridcolor=colors['grid']),
    yaxis=dict(showgrid=True, gridcolor=colors['grid'])
)

summary = past_df.describe().T
summary = summary.applymap(lambda x: round(x, 2))
summary.reset_index(inplace=True)
summary.columns = ['Metric', 'Count', 'Mean', 'Std', 'Min', '25%', '50%', '75%', 'Max']
summary_table_fig = go.Figure(data=[go.Table(
        header=dict(
            values = [f'{col}' for col in summary.columns],
            fill_color=colors['turquoise'],
            align='left',
            font=dict(color=colors['background']),
            line_color=colors['background'],
        ),
        cells=dict(
            values=[summary[col] for col in summary.columns],
            fill_color='white',
            align='center',
            font=dict(color=colors['black']),
            line_color=colors['black'],
        ),
    )])
summary_table_fig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0),
    title='Past Data Statistics',
)

fig_temp_dist = px.histogram(past_df, x='temperature', color='temperature',
                             title='Temperature Distribution',
                             labels={'temperature': 'Temperature', 'count': 'Frequency'},
                             )

fig_temp_dist.update_layout(
    plot_bgcolor=colors['plot_background'],
    paper_bgcolor=colors['background'],
    font_color=colors['black'],
    title_font=dict(size=24, family='Arial Black, sans-serif', color=colors['turquoise']),
    xaxis=dict(showgrid=True, gridcolor=colors['grid'], range=[20, None]),
    yaxis=dict(showgrid=True, gridcolor=colors['grid']),
)

fig_vib_dist = px.histogram(past_df, x='vibration', color='vibration',
                            title='Vibration Distribution',
                            labels={'vibration': 'Vibration', 'count': 'Frequency'},
                            )

fig_vib_dist.update_layout(
    plot_bgcolor=colors['plot_background'],
    paper_bgcolor=colors['background'],
    font_color=colors['black'],
    title_font=dict(size=24, family='Arial Black, sans-serif', color=colors['turquoise']),
    xaxis=dict(showgrid=True, gridcolor=colors['grid']),
    yaxis=dict(showgrid=True, gridcolor=colors['grid']),
)

app.layout = html.Div(
    style={'backgroundColor': colors['background'], 'padding': '20px', 'margin':'20px', 'fontFamily': 'Arial, sans-serif'},
    children=[
        html.Div(
            children = [
            html.Div(
                style={
                    'display': 'flex',
                    'alignItems': 'center',
                    'justifyContent': 'space-between',
                    'backgroundColor': colors['turquoise'],
                    'borderRadius': '15px',
                    'padding': '20px',
                    'paddingRight': '0px',
                    'marginLeft': '30px',
                    'height': '130px',
                    'width': '40%',
                    'opacity': '0.83',
                    'float': 'left',
                },
                children=[
                    html.H1(
                        children=["Electric Screwdriver", html.Br(), "Performance Dashboard"],
                        style={
                            'textAlign': 'center',
                            'color': colors['background'],
                            'fontFamily': 'Arial Black, sans-serif',
                            'fontSize': '35px',
                            'marginLeft': '50px',
                        }
                    ),
                ]
            ),
            html.Div(
                style={'float': 'right'},
            children=[
            html.Img(src='assets/photo2.jpg',
                    style={'width': '300px',
                        'height': '270px',
                        'marginRight': '70px',
                        'borderRadius': '15px',
                        }),
            html.Img(src='assets/photo1.jpg',
                     style={'width': '300px',
                            'height': '270px',
                            'marginRight': '50px',
                            'borderRadius': '15px',
                            }),
            ],
            ),
            ],
        ),
        html.Div(
        [
            html.H2("Current Battery Level", style={'textAlign': 'left',
                                                    'color': colors['turquoise'],
                                                    'fontFamily': 'Arial Black, sans-serif',
                                                    'marginLeft': '50px',
                                                    }),
            html.P(
                id="battery-level",
                style={'textAlign': 'left',
                        'color': colors['black'],
                        'fontSize': '24px',
                        'fontFamily': 'Arial, sans-serif',
                        'marginLeft': '50px',
                        }
            ),
        ],
        style={'marginTop': '30px', 'float': 'left'}
        ),
        html.Div(id='graphs',
            style={'marginTop': '350px', 'borderColor': colors['turquoise'], 'borderWidth': '4px', 'borderStyle': 'solid', 'borderRadius': '15px'},
            children=[

            html.Div(
                [
                    html.Div(
                        dcc.Graph(id='temp-graph', figure=fig_temp),
                        style={'width': '35%', 'display': 'inline-block', 'padding': '0px'}
                    ),
                    html.Div(
                        dcc.Graph(id='light-graph', figure=fig_light),
                        style={'width': '35%', 'display': 'inline-block', 'padding': '0px'}
                    ),
                    html.Div(
                        dcc.Graph(id='vibration-graph', figure=fig_vibration),
                        style={'width': '35%', 'display': 'inline-block', 'padding': '0px'}
                    ),
                ],
                style={'display': 'flex', 'justifyContent': 'center'}
            ),
            ],
        ),
        html.Div(id='stats',
            style={'marginTop': '40px', 'borderColor': colors['turquoise'], 'borderWidth': '4px', 'borderStyle': 'solid', 'borderRadius': '15px', 'height': '750px'},
            children=[
                html.Div(
                    [
                    html.Div(
                        dcc.Graph(id='temp-dist', figure=fig_temp_dist),
                        style={'width': '35%', 'display': 'inline-block', 'padding': '0px'}
                    ),
                    html.Div(
                        dcc.Graph(id='vib-dist', figure=fig_vib_dist),
                        style={'width': '35%', 'display': 'inline-block', 'padding': '0px'}
                    ),
                    ],
                    style={'display': 'flex', 'justifyContent': 'center'},
                ),
                html.Div(
                    dcc.Graph(figure=summary_table_fig),
                    style={'width': '80%','backgroundColor': colors['background'], 'marginLeft': '13%', 'marginTop': '50px','height': '188px','display': 'flex', 'justifyContent': 'center'},
                )
            ],
        ),
        dcc.Interval(
            id='interval-component',
            interval=2*1000,
            n_intervals=0
        ),
        dcc.ConfirmDialog(
            id='confirm-dialog',
            message='',
        ),
        html.Div(
            [
                html.P(
                    children = ["Made by: Benedetta Pacilli, Valentina Pieri, Parisa Sokuti", html.Br(), "University of Bologna - Intelligent Embedded Systems", html.Br(), "Industry 4.0 - AY 2023/2024"],
                    style={'textAlign': 'center',
                           'color': '#6B5E62',
                           'fontSize': '12px',
                           'fontFamily': 'Arial, sans-serif',
                           'marginTop': '50px',
                           }
                ),
            ],
        ),
    ]
)

data_index = 0

flags = {
    'batteryHalf': False,
    'batteryLow': False,
    'batteryCritical': False,
    'temperature': False,
    'temperatureCritical': False,
    'lowVoltage': False,
    'highVoltage': False,
    'lightLevel': False,
    'lowVibration': False,
    'highVibration': False,
}

thresholds = {
    'batteryHalf': 50,
    'batteryLow': 20,
    'batteryCritical': 5,
    'temperature': 30,
    'temperatureCritical': 50,
    'lowVoltage': 0.15,
    'highVoltage': 0.3,
    'lowLightLevel': 0.04,
    'minVibration': 1000,
    'maxVibration': 50000,
}

@app.callback(
    [Output('temp-graph', 'figure'),
     Output('light-graph', 'figure'),
     Output('vibration-graph', 'figure'),
     Output('battery-level', 'children'),
     Output('confirm-dialog', 'message'),
     Output('confirm-dialog', 'displayed')],
    [Input('interval-component', 'n_intervals'),
     Input('confirm-dialog', 'displayed')]
)

def update_graphs(n, dialog_displayed):
    global data_index

    if dialog_displayed:
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update

    data_index = (data_index + 1) % len(df)
    new_data = df.iloc[:data_index+1]

    fig_temp = px.line(new_data, x='timestamp', y='temperature', title='Real Time Temperature', color_discrete_sequence=[colors['black']])
    fig_temp.update_layout(
        plot_bgcolor=colors['plot_background'],
        paper_bgcolor=colors['background'],
        font_color=colors['black'],
        title_font=dict(size=24, family='Arial Black, sans-serif', color=colors['turquoise']),
        xaxis=dict(showgrid=True, gridcolor=colors['grid']),
        yaxis=dict(showgrid=True, gridcolor=colors['grid'])
    )

    fig_light = px.line(new_data, x='timestamp', y='lightLevel', title='Real Time Light Level', color_discrete_sequence=[colors['black']])
    fig_light.update_layout(
        plot_bgcolor=colors['plot_background'],
        paper_bgcolor=colors['background'],
        font_color=colors['black'],
        title_font=dict(size=24, family='Arial Black, sans-serif', color=colors['turquoise']),
        xaxis=dict(showgrid=True, gridcolor=colors['grid']),
        yaxis=dict(showgrid=True, gridcolor=colors['grid'])
    )

    fig_vibration = px.line(new_data, x='timestamp', y='vibration', title='Real Time Vibration', color_discrete_sequence=[colors['black']])
    fig_vibration.update_layout(
        plot_bgcolor=colors['plot_background'],
        paper_bgcolor=colors['background'],
        font_color=colors['black'],
        title_font=dict(size=24, family='Arial Black, sans-serif', color=colors['turquoise']),
        xaxis=dict(showgrid=True, gridcolor=colors['grid']),
        yaxis=dict(showgrid=True, gridcolor=colors['grid'])
    )
    current_battery_level = f"Current Battery Level: {df['battery'].iloc[data_index]}%"

    latest_data = df.iloc[data_index]
    warnings = []
    if latest_data['battery'] > thresholds['batteryHalf']:
        flags['batteryHalf'] = False
        flags['batteryLow'] = False
        flags['batteryCritical'] = False
    elif latest_data['battery'] > thresholds['batteryLow'] and latest_data['battery'] <= thresholds['batteryHalf']:
        flags['batteryLow'] = False
        flags['batteryCritical'] = False
    elif not flags['batteryCritical'] and latest_data['battery'] < thresholds['batteryCritical']:
        warnings.append(f"CRITICAL BATTERY LEVEL! Battery level below: {thresholds['batteryCritical']}%")
        flags['batteryCritical'] = True
    elif not flags['batteryLow'] and latest_data['battery'] < thresholds['batteryLow'] and latest_data['battery'] >= thresholds['batteryCritical']:
        warnings.append(f"Low battery level! Battery level is below: {thresholds['batteryLow']}%")
        flags['batteryLow'] = True
    elif not flags['batteryHalf'] and latest_data['battery'] < thresholds['batteryHalf'] and latest_data['battery'] >= thresholds['batteryLow']:
        warnings.append(f"Battery level below: {thresholds['batteryHalf']}%")
        flags['batteryHalf'] = True
    if latest_data['temperature'] < thresholds['temperatureCritical'] and latest_data['temperature'] > thresholds['temperature']:
        flags['temperatureCritical'] = False
    elif latest_data['temperature'] < thresholds['temperature']:
        flags['temperature'] = False
    if not flags['temperatureCritical'] and latest_data['temperature'] > thresholds['temperatureCritical']:
        warnings.append(f"CRITICAL TEMPERATURE! Temperature exceeded: {thresholds['temperatureCritical']}°C")
        flags['temperatureCritical'] = True
    elif not flags['temperature'] and latest_data['temperature'] > thresholds['temperature']:
        warnings.append(f"Temperature exceeded: {thresholds['temperature']}°C")
        flags['temperature'] = True
    if latest_data['lightLevel'] > thresholds['lowLightLevel']:
        flags['lightLevel'] = False
    if not flags['lightLevel'] and latest_data['lightLevel'] < thresholds['lowLightLevel']:
        warnings.append(f"Light level TOO LOW, check the working environment")
        flags['lightLevel'] = True
    if latest_data['vibration'] > thresholds['minVibration']:
        flags['lowVibration'] = False
    elif latest_data['vibration'] < thresholds['maxVibration']:
        flags['highVibration'] = False
    if not flags['lowVibration'] and latest_data['vibration'] < thresholds['minVibration']:
        warnings.append(f"Abnormal low vibration level detected, check electric screwdriver")
        flags['lowVibration'] = True
    elif not flags['highVibration'] and latest_data['vibration'] > thresholds['maxVibration']:
        warnings.append(f"Abnormal high vibration level detected, check electric screwdriver")
        flags['highVibration'] = True

    warning_message = '\n\n'.join(warnings)
    display_warning = bool(warnings)

    return fig_temp, fig_light, fig_vibration, current_battery_level, warning_message, display_warning #fig_voltage, as second

if __name__ == '__main__':
    app.run_server(debug=True)