(
  SELECT CONCAT('Podium: ', team) AS name
  FROM league
  WHERE position BETWEEN 1 AND 3
)

UNION ALL

(
  SELECT CONCAT('Demoted: ', team)
  FROM league
  WHERE position IN (14, 15)
);