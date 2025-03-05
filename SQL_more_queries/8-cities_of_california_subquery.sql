-- This script selects the id and name of cities in California using a subquery.
SELECT cities.id, cities.name FROM cities
WHERE cities.state_id IN (SELECT states.id FROM states WHERE name = 'California');