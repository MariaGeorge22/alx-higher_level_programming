-- lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server
SELECT score,
	count(score) as number
FROM second_table
GROUP BY score
ORDER BY score DESC;
