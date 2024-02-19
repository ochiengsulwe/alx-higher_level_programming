-- Script to list all cities with their respective states

-- Use the specified database passed as an argument.

-- List all cities with their respective states
SELECT cities.id, cities.name, states.name AS state_name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
