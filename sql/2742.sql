SELECT life_registry.name, ROUND(life_registry.omega * 1.618, 3) AS 'Fator N'
FROM life_registry INNER JOIN dimensions
ON life_registry.dimensions_id = dimensions.id
WHERE dimensions.name IN ('C875', 'C774') AND life_registry.name LIKE 'Richard%'
ORDER BY life_registry.omega ASC;