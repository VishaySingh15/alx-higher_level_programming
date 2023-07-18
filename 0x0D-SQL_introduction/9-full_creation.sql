-- This task creates a table and adds rows
-- Creates table second_table
CREATE TABLE IF NOT EXISTS second_table(
	id INT,
	name VARCHAR(256),
	score INT);
-- Inserts first value
INSERT INTO second_table(id, name, score)
VALUES (1, "John", 10);
-- Insert second value
INSERT INTO second_table(id, name, score)
VALUES (2, "Alex", 3);
-- Insert third value
INSERT INTO second_table(id, name, score)
VALUES (3, "Bob", 14);
-- Insert fourth value
INSERT INTO second_table(id, name, score)
VALUES (4, "George", 8);
