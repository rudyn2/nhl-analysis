

class League:
    KEEP_COLS = [
        'team',
        'gp',
        'w',
        'l'
    ]


class Skater:
    KEEP_COLS = [
        'player',
        'gp',
        'pos',
        'p',
        'g',
        'a'
    ]

    NAME_MAPPING = {
        'player': 'Jugador',
        'pos': 'Posición',
        'gp': 'Partidos jugados',
        'p': 'Puntos',
        'g': 'Goles',
        'a': 'Asistencias'
    }


class Goalie:
    KEEP_COLS = [
        'player',
        'gp',
        'w',
        'l_r',
        'l_ot'
    ]

    NAME_MAPPING = {
        'player': 'Jugador',
        'gp': 'Partidos jugados',
        'w': 'Partidos ganados',
        'l_r': 'Regular loss',
        'l_ot': 'Overtime loss'
    }


class Team:
    KEEP_COLS = [
        'team',
        'rw',
        'gf',
        'ga'
    ]

    NAME_MAPPING = {
        'team': 'Equipo',
        'season': 'Temporada',
        'gp': 'Partidos jugados',
        'w': 'Partidos ganados',
        'l': 'Partidos perdidos',
        'ot': 'Overtime Losses',
        'gf': 'Goles realizados',
        'ga': 'Goles recibidos',
        'rw': 'Regulation wins'

    }
