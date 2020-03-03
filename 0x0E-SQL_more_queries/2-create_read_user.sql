-- > This file creates a database called hbtn_0d_2 if it doesn't exists.
-- > Creates the user user_0d_2 which can only SELECT on the database hbnt_0d_2.
-- > Sets user 'user_0d_2' password to 'user_0d_2_pwd'.

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
SET PASSWORD FOR 'user_0d_2'@'localhost' = 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
