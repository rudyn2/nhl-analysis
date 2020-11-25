CREATE TABLE nhl.game_plays
(
    play_id varchar(255) NOT NULL,
    game_id bigint NOT NULL,
    play_num smallint,
    team_id_for double precision,       
    team_id_against double precision,    
    event varchar(255),                
    secondaryType varchar(255),         
    x double precision,                    
    y double precision,                     
    period bigint,               
    periodType varchar(255),            
    periodTime smallint,          
    periodTimeRemaining smallint,   
    dateTime timestamp without time zone,             
    goals_away smallint,            
    goals_home smallint,            
    description varchar(255),           
    st_x double precision,                  
    st_y double precision,                  
    rink_side varchar(255),             
    PRIMARY KEY (play_id)
)
TABLESPACE pg_default;

ALTER TABLE nhl.game_plays
    OWNER to cc3201;