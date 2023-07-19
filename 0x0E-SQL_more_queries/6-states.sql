-- This task creates a db and table
-- Creates db
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use db hbtn_0d_usa
USE hbtn_0d_usa;
-- Creates table
CREATE TABLE IF NOT EXISTS states(
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL);
