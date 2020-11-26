-- Table: nhl.game

-- DROP TABLE nhl.game;

CREATE TABLE nhl.game
(
    game_id bigint NOT NULL,
    season bigint,
    type "char",
    date_time date,
    "date_time_GMT" timestamp with time zone,
    away_team_id smallint,
    home_team_id smallint,
    away_goals smallint,
    home_goals smallint,
    outcome varchar(255),
    home_rink_side_start varchar(255),
    venue varchar(255),
    venue_link varchar(255),
    venue_time_zone_id varchar(255),
    venue_time_zone_offset smallint,
    venue_time_zone_tz varchar(255),
    PRIMARY KEY (game_id)
)
TABLESPACE pg_default;

ALTER TABLE nhl.game
    OWNER to cc3201;