import psycopg2
import pandas as pd
import os


class NHLProxy:
    def __init__(self, connection, queries_path: str):
        self.conn = connection
        self.queries_path = queries_path

    def _execute(self, sql_file: str, headers: list) -> pd.DataFrame:
        cursor = self.conn.cursor()
        with cursor as cursor:
            cursor.execute(open(sql_file, "r").read())
            if headers:
                return pd.DataFrame(cursor.fetchall(), columns=headers)
            return pd.DataFrame(cursor.fetchall())

    def get_team_info(self):
        headers = ['team_id', 'franchiseid', 'shortname', 'teamname', 'abbreviation', 'link']
        return self._execute(os.path.join(self.queries_path, 'get_team_info.sql'), headers)

    def get_team_abbreviations(self):
        team_all_info = self.get_team_info()
        team_all_info['full_name'] = team_all_info['shortname'] + ' ' + team_all_info['teamname']
        return dict(zip(team_all_info['abbreviation'], team_all_info['full_name']))

    def get_team_stats(self):
        headers = ['team', 'season', 'gp', 'w', 'l', 'ot', 'rw', 'rot', 'sow', 'gf', 'ga', 'div_gf_gp',
                   'div_ga_gp', 'div_sf_gp', 'div_sa_gp']
        return self._execute(os.path.join(self.queries_path, 'teams.sql'), headers)

    def get_goalie_stats(self):
        headers = ['player', 'season', 'team', 'gp', 'w', 'l_r', 'l_ot', 'sa', 'svs', 'ga', 'svp',
                   'gaa', 'toi', 'so', 'g', 'a', 'pim']
        return self._execute(os.path.join(self.queries_path, 'goalies.sql'), headers)

    def get_skater_stats(self):
        headers = ['player', 'season', 'team', 'pos', 'gp', 'g', 'a', 'p', 'pm', 'pim', 'div_p_gp',
                   'ppg', 'ppp', 'shg', 'shp', 's', 's_per', 'div_toi_gp']
        return self._execute(os.path.join(self.queries_path, 'skaters.sql'), headers)

