-- create database if doesn't exist
SELECT tv_shows.title,
	tv_show_genres.genre_id
from tv_shows
	LEFT OUTER JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.genre_id is NULL
ORDER BY tv_shows.title,
	tv_show_genres.genre_id;
