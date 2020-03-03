-- This script shows the privileges of the users user_0d_1 and user_0d_2 on the
-- server 'localhost'
FLUSH PRIVILEGES;
SHOW GRANTS FOR user_0d_1@localhost;
SHOW GRANTS FOR user_0d_2@localhost;
