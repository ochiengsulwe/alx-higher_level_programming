-- Script to list cities of California without using JOIN
CREATE IF NOT EXISTS hbtn_0d_usa;
-- Use the specified database passed as an argument
USE hbtn_0d_usa;

-- List all cities of California
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id AND states.name = 'California'
ORDER BY cities.id ASC;
