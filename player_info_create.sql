CREATE TABLE nhl.player_info
(
    player_id bigint NOT NULL,
    firstName varchar(255),
    lastName varchar(255),
    nationality varchar(255),
    birthCity varchar(255),
    primaryPosition varchar(255),
    birthDate date,
    link varchar(255),
    PRIMARY KEY (player_id)
)
TABLESPACE pg_default;

ALTER TABLE nhl.playe_info
    OWNER to cc3201;