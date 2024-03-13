-- create database if doesn't exist
SELECT tv_shows.title
from tv_shows
WHERE tv_shows.title NOT IN (
		SELECT tv_shows.title
		from tv_genres
			JOIN tv_show_genres ON (tv_genres.ID = tv_show_genres.genre_id)
			JOIN tv_shows ON(tv_shows.id = tv_show_genres.show_id)
		WHERE tv_genres.name = 'Comedy'
	)
ORDER BY tv_shows.title ASC;
