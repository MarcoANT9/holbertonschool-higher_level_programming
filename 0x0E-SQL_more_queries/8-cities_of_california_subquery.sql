-- > This script lists all the cities of "California" found in the database
--   hbtn_0d_usa.

SELECT (SELECT id FROM hbtn_0d_usa.states WHERE name = "California"), name
FROM hbtn_0d_usa.cities ORDER BY name ASC;
