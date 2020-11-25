CREATE TABLE nhl.team_info
(
    team_id bigint NOT NULL,
    franchiseId smallint,
    shortName varchar(255),
    teamName varchar(255),
    abbreviation varchar(255),
    link varchar(255),
    PRIMARY KEY (team_id)
)
TABLESPACE pg_default;

ALTER TABLE nhl.game
    OWNER to cc3201;