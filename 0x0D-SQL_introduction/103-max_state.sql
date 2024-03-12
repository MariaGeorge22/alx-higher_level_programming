-- lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server
SELECT state,
	MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
