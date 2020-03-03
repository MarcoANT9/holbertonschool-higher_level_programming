-- > This script creates a table 'force_name' in the database inserted as
--   argument
-- > The table contains two columns: id (INT) and name (VARCHAR) not null.
CREATE TABLE IF NOT EXISTS force_name(
       id INT,
       name VARCHAR(256) NOT NULL
       );
