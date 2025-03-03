-- This SQL command selects the 'score' and counts the number of occurrences of each 'score' in 'second_table'
-- The results are grouped by 'score' and ordered by 'score' in descending order
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score
ORDER BY score DESC;