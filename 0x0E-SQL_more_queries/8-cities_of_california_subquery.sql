-- > This script lists all the cities of "California" found in the database
--   hbtn_0d_usa.

SELECT id, name
FROM hbtn_0d_usa.cities
WHERE state_id = 1 IN ( SELECT `id`
      	       	      	FROM hbtn_0d_usa.states
			WHERE name = "California")
;
