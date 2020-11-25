CREATE TABLE nhl.game_goalie_stats
(
    game_id bigint NOT NULL,
    player_id bigint NOT NULL,
    team_id bigint NOT NULL,
    timeOnIce smallint,                     
    assists smallint,                      
    goals smallint,                       
    pim smallint,                          
    shots smallint,                        
    saves smallint,                      
    powerPlaySaves smallint,             
    shortHandedSaves smallint,            
    evenSaves smallint,                    
    shortHandedShotsAgainst smallint,      
    evenShotsAgainst smallint,             
    powerPlayShotsAgainst smallint,      
    decision varchar(255),                     
    savePercentage double precision,               
    powerPlaySavePercentage double precision,      
    evenStrengthSavePercentage double precision,   
    FOREIGN KEY (game_id) REFERENCES nhl.game(game_id), 
    FOREIGN KEY (player_id) REFERENCES nhl.player_info(player_id),
    FOREIGN KEY (team_id) REFERENCES nhl.team_info(team_id),
    PRIMARY KEY (game_id, player_id, team_id)
)
TABLESPACE pg_default;

ALTER TABLE nhl.game
    OWNER to cc3201;