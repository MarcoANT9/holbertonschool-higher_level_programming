-- > This script creates a table 'cities' in the database hbtn_0d_usa
-- > states:
--	id -> INT UNIQUE AUTO_GENERATED NOT NULL PRIMARY KEY
--	state_id -> INT NOT NULL FOREIGN KEY(references id of states table)
--	name -> VARCHAR(256), can't be null.

/* Creates Database */
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

/* Creates Table */
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(

       id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL,

       FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.state(id)
);
