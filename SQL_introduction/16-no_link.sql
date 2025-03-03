-- This SQL command selects the 'score' and 'name' from 'second_table' where 'name' is not null
-- The results are ordered by 'score' in descending order
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;