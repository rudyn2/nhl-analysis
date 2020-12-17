# Import required libraries
import pathlib

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import plotly.express as px
import psycopg2
from dash.dash import no_update
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import sys
import os
from pathlib import Path

sys.path.append(Path(os.getcwd()).parent.parent)
sys.path.append(Path(os.getcwd()).parent)
sys.path.append(Path(os.getcwd()))

from dashboard.config import *
from dashboard.nhl_proxy import NHLProxy

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
app.title = 'NHL Stats'
server = app.server
params = {
    'database': 'nhl-db',
    'user': 'cc3201',
    'password': 'sup3rs3cur3',
    'host': 'cc3201.dcc.uchile.cl',
    'port': 5524
}
conn = psycopg2.connect(**params)
n = NHLProxy(conn, 'queries')
team_stats = n.get_team_stats()
skater = n.get_skater_stats()
goalie = n.get_goalie_stats()
team_abbreviation_dict = n.get_team_abbreviations()

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
                            id="season_selector",
                            options=[
                                {'label': f'{i}-{i + 1}', 'value': i} for i in range(2015, 2019)
                            ],
                            clearable=False,
                            value=2015
                        ),
                        html.P(
                            "Filtra por tipo de temporada",
                            className="control_label",
                        ),
                        dcc.RadioItems(
                            id="type_season_selector",
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
                            id='team_selector',
                            options=[
                                {'label': f'Equipo-{i}', 'value': i} for i in range(10)
                            ],
                            placeholder="Equipo A"
                        ),
                    ],
                    className="pretty_container four columns",
                    id="cross-filter-options",
                    # style={'height': '500px'}
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [html.H6(id="total_plays", children=10), html.P("Partidos jugados")],
                                    id="wells",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="total_win", children=6), html.P("Partidos ganados")],
                                    id="gas",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="total_lost", children=4), html.P("Partidos perdidos")],
                                    id="oil",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="overtime_loss", children=0), html.P("Overtime loss")],
                                    id="water",
                                    className="mini_container",
                                ),
                            ],
                            id="info-container",
                            className="row container-display",
                        ),
                        html.Div(
                            [dash_table.DataTable(
                                id='team_stats_table',
                                style_cell={'textAlign': 'center',
                                            'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                            'whiteSpace': 'normal'},
                                style_header={
                                    'backgroundColor': 'rgb(230, 230, 230)',
                                    'fontWeight': 'bold'
                                },
                                style_data_conditional=[
                                    {
                                        'if': {'row_index': 'odd'},
                                        'backgroundColor': 'rgb(248, 248, 248)'
                                    }
                                ],
                                fixed_rows={'headers': True},
                                style_table={'height': '30%', 'overflowY': 'auto'}
                                # id='table',
                                # columns=[{"name": i, "id": i} for i in df.columns],
                                # data=df.to_dict('records'),
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
                    [
                        dcc.Graph(id='league_ranking_graph')],
                    className="pretty_container twelve columns",
                )
            ],
            id='league_ranking_div',
            className="row flex-display"
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.H5("Skater stats"),
                        dash_table.DataTable(
                            id='skater_stats',
                            style_cell={'textAlign': 'center',
                                        'minWidth': '50px', 'width': '40px', 'maxWidth': '180px',
                                        'whiteSpace': 'normal'},
                            style_header={
                                'backgroundColor': 'rgb(230, 230, 230)',
                                'fontWeight': 'bold',
                                'z-index': '5px'
                            },
                            style_data_conditional=[
                                {
                                    'if': {'row_index': 'odd'},
                                    'backgroundColor': 'rgb(248, 248, 248)'
                                }
                            ],
                            fixed_rows={'headers': True},
                            style_table={'height': '30%', 'overflowY': 'auto'}
                        )],
                    className="pretty_container six columns",
                ),
                html.Div(
                    [
                        html.H5("Goalie Stats"),
                        dash_table.DataTable(
                            id='goalie_stats',
                            style_cell={'textAlign': 'center',
                                        'minWidth': '50px', 'width': '100px', 'maxWidth': '180px',
                                        'whiteSpace': 'normal'},
                            style_header={
                                'backgroundColor': 'rgb(230, 230, 230)',
                                'fontWeight': 'bold'
                            },
                            style_data_conditional=[
                                {
                                    'if': {'row_index': 'odd'},
                                    'backgroundColor': 'rgb(248, 248, 248)'
                                }
                            ],
                            fixed_rows={'headers': True},
                            style_table={'height': '30%', 'overflowY': 'auto'}
                        )],
                    className="pretty_container six columns",
                ),
            ],
            id="detail_team_stats",
            className="row flex-display",
        )
    ],
    id="mainContainer",
    style={"display": "flex", "flex-direction": "column"},
)


def abbreviation2name(s: str, map_dict: dict) -> str:
    if '-' in s:
        return map_dict[s.split('-')[0]]
    return map_dict[s]


def process_stats(df_stats: pd.DataFrame, team: str, keep_cols: list, team_dict: dict) -> pd.DataFrame:
    sub_df = df_stats.copy()
    sub_df['team'] = sub_df['team'].map(lambda x: abbreviation2name(x, team_dict))
    sub_df = sub_df[sub_df['team'] == team]
    sub_df = sub_df[keep_cols]
    return sub_df


@app.callback(Output("team_selector", "options"),
              [Input("season_selector", "value"),
               Input("type_season_selector", "value")])
def update_team_selector(season, type_season):
    sub_df = team_stats[team_stats['season'] == int(f'{season}{season + 1}')]
    teams = list(sub_df['team'].values)
    options = [{'label': team, 'value': team} for team in teams]
    return options


@app.callback([Output("team_stats_table", "data"),
               Output("team_stats_table", "columns"),
               Output("total_plays", "children"),
               Output("total_win", "children"),
               Output("total_lost", "children"),
               Output("overtime_loss", "children"),
               Output("info-container", "style"),
               Output("league_ranking_graph", "figure"),
               Output("league_ranking_div", "style")],
              [Input("season_selector", "value"),
               Input("type_season_selector", "value"),
               Input("team_selector", "value")])
def update_team_stats_table(season, type_season, team):
    if not season:
        raise PreventUpdate

    sub_df = team_stats[team_stats['season'] == int(f'{season}{season + 1}')]
    if team:
        # return metrics of a specific team
        sub_df = sub_df[sub_df['team'] == team]
        total = sub_df['gp']
        win = sub_df['w']
        lost = sub_df['l']
        ot = sub_df['ot']
        sub_df = sub_df[Team.KEEP_COLS]
        new_info_container_class = {'display': 'flex'}

        # league ranking
        league_ranking_style = {'display': 'none'}
        league_ranking_graph = no_update
    else:
        # return entire league and hide mini containers
        sub_df = sub_df[League.KEEP_COLS]
        sub_df.sort_values(by='w', axis=0, inplace=True, ascending=False)
        total = win = lost = ot = no_update

        # league ranking
        new_info_container_class = {'display': 'none'}
        league_ranking_style = {'display': 'flex'}
        sub_df = sub_df.rename(columns=Team.NAME_MAPPING)
        fig = px.bar(sub_df, y='Partidos ganados', x='Equipo', text='Partidos ganados')
        fig.update_traces(texttemplate='%{Partidos ganados:.2s}', textposition='outside')
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        league_ranking_graph = fig

    # data-table attributes
    sub_df = sub_df.rename(columns=Team.NAME_MAPPING)
    cols = [{"name": i, "id": i} for i in sub_df.columns]

    return sub_df.to_dict('records'), cols, total, win, lost, ot, \
           new_info_container_class, league_ranking_graph, league_ranking_style


@app.callback([Output("skater_stats", "data"),
               Output("goalie_stats", "data"),
               Output("skater_stats", "columns"),
               Output("goalie_stats", "columns"),
               Output("detail_team_stats", "style")],
              [Input("season_selector", "value"),
               Input("type_season_selector", "value"),
               Input("team_selector", "value")])
def update_skater_stats(season, type_season, team):
    if not season:
        raise PreventUpdate

    if team:
        sub_df_skater = skater[skater['season'] == int(f'{season}{season + 1}')].copy()
        sub_df_goalie = goalie[goalie['season'] == int(f'{season}{season + 1}')].copy()
        sub_df_skater = process_stats(sub_df_skater, team, Skater.KEEP_COLS, team_abbreviation_dict)
        sub_df_goalie = process_stats(sub_df_goalie, team, Goalie.KEEP_COLS, team_abbreviation_dict)
        sub_df_skater = sub_df_skater.rename(columns=Skater.NAME_MAPPING)
        sub_df_goalie = sub_df_goalie.rename(columns=Goalie.NAME_MAPPING)
        skater_cols = [{"name": i, "id": i} for i in sub_df_skater.columns]
        goalie_cols = [{"name": i, "id": i} for i in sub_df_goalie.columns]

        return sub_df_skater.to_dict("records"), sub_df_goalie.to_dict("records"), \
               skater_cols, goalie_cols, {'display': 'flex'}
    else:
        skater_data = goalie_data = skater_cols = goalie_cols = no_update
        skater_goalie_stats_display = {'display': 'none'}

    return skater_data, goalie_data, skater_cols, goalie_cols, skater_goalie_stats_display


if __name__ == "__main__":
    app.run_server(debug=True)
