CREATE TABLE nhl.game_plays_players
(
	play_id varchar(255) NOT NULL,
    game_id bigint NOT NULL,
	play_num smallint NOT NULL,
	player_id bigint NOT NULL,
	playerType varchar(255),
    FOREIGN KEY (play_id) REFERENCES nhl.game_plays(play_id), 
    FOREIGN KEY (game_id) REFERENCES nhl.game(game_id),
    FOREIGN KEY (player_id) REFERENCES nhl.player_info(player_id),
    PRIMARY KEY (play_id, game_id, player_id, playerType)
)
TABLESPACE pg_default;

ALTER TABLE nhl.game_plays_players
    OWNER to cc3201;
