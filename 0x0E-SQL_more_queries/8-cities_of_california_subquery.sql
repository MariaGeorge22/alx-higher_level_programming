-- list all the cities of California that can be found in the database hbtn_0d_usa 
SELECT id,
	name
from cities
WHERE (
		SELECT id
		from states
		WHERE (
				cities.state_id = states.id
				AND states.name = 'California'
			)
	)
ORDER BY cities.id;
