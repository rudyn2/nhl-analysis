SELECT team_info.shortname || ' ' || team_info.teamname as equipo, game.season,
COUNT(gts.game_id) as GP,
COUNT(CASE WHEN won THEN 0 END) as W,
COUNT(CASE WHEN NOT won THEN 0 END) as L,
COUNT(CASE WHEN settled_in='OT' THEN 0 END) as OT,
COUNT(CASE WHEN won AND settled_in='REG' THEN 0 END) as RW,
COUNT(CASE WHEN won AND settled_in='OT' THEN 0 END) as ROT,
COUNT(CASE WHEN won AND settled_in='SO' THEN 0 END) as SOW,
SUM(gts.goals) as GF,
SUM(gts.goalsa) AS GA,
CAST(SUM(gts.goals) AS FLOAT(10))/CAST(COUNT(gts.game_id) AS FLOAT(10)) AS div_GF_GP,
CAST(SUM(gts.goalsa) AS FLOAT(10))/CAST(COUNT(gts.game_id) AS FLOAT(10)) AS div_GA_GP,
CAST(SUM(gts.shots) AS FLOAT(10))/CAST(COUNT(gts.game_id) AS FLOAT(10)) AS div_SF_GP,
CAST(SUM(gts.shotsa) AS FLOAT(10))/CAST(COUNT(gts.game_id) AS FLOAT(10)) AS div_SA_GP
FROM (
	SELECT A.game_id,A.team_id,A.hoa,A.won,A.settled_in,A.head_coach,A.goals,A.shots,A.hits,A.pim,A.powerplayopportunities,A.powerplaygoals,A.faceoffwinpercentage,A.giveaways,A.takeaways,B.goals AS goalsa, B.shots AS shotsa
	FROM nhl.game_team_stats A, nhl.game_team_stats B
	WHERE A.game_id=B.game_id AND A.team_id<>B.team_id
) gts
INNER JOIN nhl.team_info ON team_info.team_id=gts.team_id
INNER JOIN nhl.game ON gts.game_id=game.game_id
GROUP BY gts.team_id, equipo, season
ORDER BY season, equipo ASC;