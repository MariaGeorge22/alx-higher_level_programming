-- lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server
SELECT city,
	AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
