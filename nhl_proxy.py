import psycopg2
import pandas as pd
import os


class NHLProxy:
    def __init__(self, cursor, queries_path: str):
        self.cursor = cursor
        self.queries_path = queries_path

    def _execute(self, sql_file: str, headers: list) -> pd.DataFrame:
        with self.cursor as cursor:
            cursor.execute(open(sql_file, "r").read())
            if headers:
                return pd.DataFrame(cursor.fetchall(), columns=headers)
            return pd.DataFrame(cursor.fetchall())

    def get_team_info(self):
        headers = ['team_id', 'franchiseid', 'shortname', 'teamname', 'abbreviation', 'link']
        return self._execute(os.path.join(self.queries_path, 'get_team_info.sql'), headers)


if __name__ == '__main__':
    params = {
        'database': 'nhl-db',
        'user': 'cc3201',
        'password': 'sup3rs3cur3',
        'host': 'cc3201.dcc.uchile.cl',
        'port': 5524
    }

    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    n = NHLProxy(cur, './queries')
    team_info = n.get_team_info()
