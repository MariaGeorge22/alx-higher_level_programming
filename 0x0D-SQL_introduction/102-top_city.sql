-- lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server
SELECT city,
	AVG(value) AS avg_temp
FROM temperatures
WHERE (
		month = 7
		OR month = 8
	)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
