SELECT player_info.firstname || ' ' ||  player_info.lastname as player, 
game.season,
STRING_AGG(DISTINCT team_info.abbreviation,'-') as Team,
STRING_AGG(DISTINCT player_info.primaryposition,'-') as Pos,
COUNT(gss.game_id) as GP,
SUM(gss.goals) as G,
SUM(gss.assists) as A,
SUM(gss.goals) + SUM(gss.assists) as P,
SUM(gss.plusminus) as PM,
SUM(gss.penaltyminutes) as PIM,
CAST(SUM(gss.goals) + SUM(gss.assists) AS FLOAT(10))/CAST(COUNT(gss.game_id) AS FLOAT(10)) AS div_P_GP,
SUM(gss.powerplaygoals) as PPG,
SUM(gss.powerplaygoals) + SUM(gss.powerplayassists) as PPP,
SUM(gss.shorthandedgoals) as SHG,
SUM(gss.shorthandedgoals) + SUM(gss.shorthandedassists) as SHP,
SUM(gss.shots) as S,
CAST(SUM(gss.goals)*100 AS FLOAT(10)) / NULLIF(CAST(SUM(gss.shots) AS FLOAT(10)), 0) as S_per,
SUM(gss.timeonice)/COUNT(gss.game_id)/60 || ':' || SUM(gss.timeonice)/COUNT(gss.game_id)%60 as div_TOI_GP
FROM nhl.game_skater_stats gss
INNER JOIN nhl.player_info ON player_info.player_id=gss.player_id
INNER JOIN nhl.game ON gss.game_id=game.game_id
INNER JOIN nhl.team_info ON gss.team_id=team_info.team_id
GROUP BY gss.player_id, player, season
ORDER BY season, P DESC;