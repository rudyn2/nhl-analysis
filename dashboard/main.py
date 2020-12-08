# Import required libraries
import pickle
import copy
import pathlib
import urllib.request
import dash
import math
import datetime as dt
import pandas as pd
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_table
# Multi-dropdown options
from controls import COUNTIES, WELL_STATUSES, WELL_TYPES, WELL_COLORS


# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
app.title = 'NHL Stats'
server = app.server
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

# Create app layout
app.layout = html.Div(
    [
        dcc.Store(id="aggregate_data"),
        # empty Div to trigger javascript file for graph resizing
        html.Div(id="output-clientside"),
        html.Div(
            [
                html.Div(
                    [
                        html.Img(
                            src=app.get_asset_url("nhl-logo.png"),
                            id="plotly-image",
                            style={
                                "height": "60px",
                                "width": "auto",
                                "margin-bottom": "25px",
                            },
                        )
                    ],
                    className="one-third column",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3(
                                    "NHL Stats",
                                    style={"margin-bottom": "0px"},
                                ),
                                html.H5(
                                    "Proyecto Bases de Datos", style={"margin-top": "0px"}
                                ),
                            ]
                        )
                    ],
                    className="one-half column",
                    id="title",
                ),
                html.Div(
                    [
                        html.A(
                            html.Button("Repo", id="learn-more-button"),
                            href="https://github.com/rudyn2/nhl-analysis",
                        )
                    ],
                    className="one-third column",
                    id="button",
                ),
            ],
            id="header",
            className="row flex-display",
            style={"margin-bottom": "25px"},
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.P(
                            "Filtra por temporada",
                            className="control_label",
                        ),
                        dcc.Dropdown(
                            options=[
                                {'label': f'{i}-{i+1}', 'value': i} for i in range(2015, 2019)
                            ],
                            value=2015
                        ),
                        html.P(
                            "Filtra por tipo de temporada",
                            className="control_label",
                        ),
                        dcc.RadioItems(
                            id="well_status_selector",
                            options=[
                                {"label": "Regular ", "value": "regular"},
                                {"label": "Play-Off", "value": "play-off"}
                            ],
                            value="regular",
                            labelStyle={"display": "inline-block"},
                            className="dcc_control",
                        ),
                        html.P(
                            "Filtra por equipo",
                            className="control_label",
                        ),
                        dcc.Dropdown(
                            options=[
                                {'label': f'Equipo-{i}', 'value': i} for i in range(10)
                            ],
                            value=0
                        ),
                    ],
                    className="pretty_container four columns",
                    id="cross-filter-options",
                    style={'height': '500px'}
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [html.H6(id="well_text", children=10), html.P("Partidos jugados")],
                                    id="wells",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="gasText", children=6), html.P("Partidos ganados")],
                                    id="gas",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="oilText", children=4), html.P("Partidos perdidos")],
                                    id="oil",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="waterText", children=0), html.P("Metric")],
                                    id="water",
                                    className="mini_container",
                                ),
                            ],
                            id="info-container",
                            className="row container-display",
                        ),
                        html.Div(
                            [html.P("Aquí va la tabla con stats de jugadores en el equipo seleccionado"),
                             dash_table.DataTable(
                                id='table',
                                columns=[{"name": i, "id": i} for i in df.columns],
                                data=df.to_dict('records'),
                            )],
                            id="countGraphContainer",
                            className="pretty_container",
                        ),
                    ],
                    id="right-column",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.Div(
                    [dcc.Graph(id="main_graph")],
                    className="pretty_container seven columns",
                ),
                html.Div(
                    [dcc.Graph(id="individual_graph")],
                    className="pretty_container five columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.Div(
                    [dcc.Graph(id="pie_graph")],
                    className="pretty_container seven columns",
                ),
                html.Div(
                    [dcc.Graph(id="aggregate_graph")],
                    className="pretty_container five columns",
                ),
            ],
            className="row flex-display",
        ),
    ],
    id="mainContainer",
    style={"display": "flex", "flex-direction": "column"},
)


# Main
if __name__ == "__main__":
    app.run_server(debug=True)