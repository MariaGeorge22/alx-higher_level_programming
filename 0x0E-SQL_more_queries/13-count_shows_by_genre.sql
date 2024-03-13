-- create database if doesn't exist
SELECT tv_genres.name AS genre,
	count(tv_show_genres.show_id) AS number_of_shows
from tv_genres
	JOIN tv_show_genres ON (tv_genres.ID = tv_show_genres.genre_id)
	JOIN tv_shows ON(tv_shows.id = tv_show_genres.show_id)
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
