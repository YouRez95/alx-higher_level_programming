-- lists all cities contained in the databse
SELECT c.id, c.name, s.name
FROM cities c
JOIN states s ON c.state_id = s.id;
