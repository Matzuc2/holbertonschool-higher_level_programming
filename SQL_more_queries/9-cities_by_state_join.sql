-- This script selects the id and name of cities along with the name of their corresponding state using a join.
SELECT cities.id, cities.name, states.name FROM cities
INNER JOIN states ON cities.state_id = states.id;