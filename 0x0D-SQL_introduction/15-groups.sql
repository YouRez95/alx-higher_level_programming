-- count
SELECT score, COUNT(score) AS 'number' FROM second_table GROUP BY score HAVING COUNT(score) > 0 ORDER BY SCORE DESC;
