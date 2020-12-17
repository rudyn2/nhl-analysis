SELECT player_info.firstname || ' ' || player_info.lastname as player, game.season,
STRING_AGG(DISTINCT team_info.abbreviation,'-') as team,
COUNT(ggs.game_id) as GP,
COUNT(CASE WHEN nhl.game_team_stats.won THEN 0 END) as W,
COUNT(CASE WHEN NOT nhl.game_team_stats.won AND nhl.game_team_stats.settled_in='REG' THEN 0 END) as L_R,
COUNT(CASE WHEN NOT nhl.game_team_stats.won AND nhl.game_team_stats.settled_in='OT' THEN 0 END) as L_OT,
SUM(ggs.shots) AS SA,
SUM(ggs.saves) as SVS,
SUM(ggs.shots)-SUM(ggs.saves) AS GA,
CAST(AVG(ggs.savePercentage)/100 AS FLOAT(10)) as SVP,
CAST(AVG(ggs.shots-ggs.saves) AS FLOAT(10)) as GAA,
CAST(SUM(ggs.timeonice)/60 AS VARCHAR) ||':'|| CAST(SUM(ggs.timeonice)%60 AS VARCHAR) as TOI,
COUNT(CASE WHEN nhl.game_team_stats.settled_in='SO' THEN 0 END) as SO,
SUM(ggs.goals) AS G,
SUM(ggs.assists) AS A,
SUM(ggs.pim) as PIM
FROM nhl.game_goalie_stats ggs
INNER JOIN nhl.player_info ON player_info.player_id=ggs.player_id
INNER JOIN nhl.game ON ggs.game_id=game.game_id
INNER JOIN nhl.team_info ON ggs.team_id=team_info.team_id
INNER JOIN nhl.game_team_stats ON ggs.game_id=nhl.game_team_stats.game_id AND ggs.team_id=nhl.game_team_stats.team_id
GROUP BY ggs.player_id, player, season
ORDER BY season, gp DESC;