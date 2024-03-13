-- create database if doesn't exist
SELECT tv_shows.title,
	tv_genres.name
from tv_genres
	JOIN tv_show_genres ON (tv_genres.ID = tv_show_genres.genre_id)
	RIGHT OUTER JOIN tv_shows ON(tv_shows.id = tv_show_genres.show_id)
ORDER BY tv_shows.title,
	tv_genres.name;
