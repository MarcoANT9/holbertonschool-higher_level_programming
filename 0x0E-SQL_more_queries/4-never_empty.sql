-- > This script creates a table 'id_not_null' in the database inserted as
--   argument
-- > The table contains two columns:
--   	 id (INT) default to 1
--   	 name (VARCHAR)

CREATE TABLE IF NOT EXISTS id_not_null(
       id INT DEFAULT 1,
       name VARCHAR(256)
       );
