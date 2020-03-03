-- > This script creates a table 'unique_id' in the database inserted as
--   argument
-- > The table contains two columns:
--   	 id (INT) defaults to 1, unique.
--   	 name (VARCHAR).

CREATE TABLE IF NOT EXISTS unique_id(
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
       );
