-- > This script creates a table 'states' in the database hbtn_0d_usa
-- > states:
--	id -> INT, UNIQUE, auto-generated can't be null and is a Primary Key...
--	name -> VARCHAR(256), can't be null.

/* Creates Database */
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

/* Creates Table */
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
       id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
       name VARCHAR(256) NOT NULL
);
