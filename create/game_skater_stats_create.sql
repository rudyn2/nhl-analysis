CREATE TABLE nhl.game_skater_stats
(
    game_id bigint NOT NULL,
    player_id bigint NOT NULL,
    team_id bigint NOT NULL,
    timeOnIce smallint,
    assists smallint,
    goals smallint,         
    shots smallint,
    hits smallint,
    powerPlayGoals smallint,
    powerPlayAssists smallint,
    penaltyMinutes smallint,
    faceOffWins smallint,
    faceoffTaken smallint,
    takeaways smallint,
    giveaways smallint,
    shortHandedGoals smallint,
    shortHandedAssists smallint,
    blocked smallint,
    plusMinus smallint,             
    evenTimeOnIce smallint,
    shortHandedTimeOnIce smallint,
    powerPlayTimeOnIce smallint,
    FOREIGN KEY (game_id) REFERENCES nhl.game(game_id), 
    FOREIGN KEY (player_id) REFERENCES nhl.player_info(player_id),
    FOREIGN KEY (team_id) REFERENCES nhl.team_info(team_id),
    PRIMARY KEY (game_id, player_id, team_id)
)
TABLESPACE pg_default;

ALTER TABLE nhl.game_skater_stats
    OWNER to cc3201;