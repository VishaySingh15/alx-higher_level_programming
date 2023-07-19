-- This task lists all Cities in California
-- Select Cities
SELECT id, name FROM cities
WHERE state_id = ( -- Get California state id
	SELECT id FROM states
	WHERE name = "California")
ORDER BY id;
