CREATE TABLE nhl.game_team_stats
(
    game_id bigint NOT NULL,
	team_id bigint NOT NULL,
	HoA varchar(255),
	won boolean,
	settled_in varchar(255),
	head_coach varchar(255),           
	goals smallint,                    
	shots smallint,                     
	hits smallint,                      
	pim smallint,                       
	powerPlayOpportunities smallint,
	powerPlayGoals smallint,         
	faceOffWinPercentage double precision,
	giveaways smallint,
	takeaways smallint,
    FOREIGN KEY (game_id) REFERENCES nhl.game(game_id), 
    FOREIGN KEY (team_id) REFERENCES nhl.team_info(team_id),
    PRIMARY KEY (game_id, team_id)
)
TABLESPACE pg_default;

ALTER TABLE nhl.game_team_stats
    OWNER to cc3201;
