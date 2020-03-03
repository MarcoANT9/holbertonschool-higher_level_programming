-- > This script creates a table 'cities' in the database hbtn_0d_usa
-- > states:
--	id -> INT UNIQUE AUTO_GENERATED NOT NULL PRIMARY KEY
--	state_id -> INT NOT NULL FOREIGN KEY(references id of states table)
--	name -> VARCHAR(256), can't be null.

/* Creates Database */
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa AS usa;

/* Creates Table */
CREATE TABLE IF NOT EXISTS usa.cities(
       id INT UNIQUE AUTO_GENERATED NOT NULL PRIMARY KEY,
       state_id INT NOT NULL FOREIGN KEY(id) REFERENCES states(id),
       name VARCHAR(256) NOT NULL
);
