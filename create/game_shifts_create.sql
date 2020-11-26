CREATE TABLE nhl.game_shifts
(
    game_id bigint NOT NULL,
    player_id bigint NOT NULL,
    period smallint NOT NULL,
    shift_start smallint,
    shift_end smallint,
    FOREIGN KEY (game_id) REFERENCES nhl.game(game_id), 
    FOREIGN KEY (player_id) REFERENCES nhl.player_info(player_id)
)
TABLESPACE pg_default;

ALTER TABLE nhl.game_shifts
    OWNER to cc3201;

-- no hay llaves primarias porque no existen llaves candidatas no triviales