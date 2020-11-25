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
    outcome text COLLATE pg_catalog."default",
    home_rink_side_start text COLLATE pg_catalog."default",
    venue text COLLATE pg_catalog."default",
    venue_link text COLLATE pg_catalog."default",
    venue_time_zone_id text COLLATE pg_catalog."default",
    venue_time_zone_offset smallint,
    venue_time_zone_tz text COLLATE pg_catalog."default",
    CONSTRAINT game_pkey PRIMARY KEY (game_id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE nhl.game
    OWNER to cc3201;