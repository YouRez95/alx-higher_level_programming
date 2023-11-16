-- list all cities of california
-- using subqueries
SELECT cities.id, cities.name
FROM cities
WHERE state_id = (
	SELECT states.id
	FROM states
	WHERE name = 'California' 
)
ORDER BY id ASC;
