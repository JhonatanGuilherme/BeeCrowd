SELECT candidate.name,
  ROUND((SELECT (score.math * 2 + score.specific * 3 + score.project_plan * 5) / 10
    FROM score
    WHERE score.candidate_id = candidate.id
  ), 2) AS avg
FROM candidate
ORDER BY avg DESC;