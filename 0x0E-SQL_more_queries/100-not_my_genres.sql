-- create database if doesn't exist
SELECT tv_genres.name
from tv_genres
WHERE tv_genres.name NOT IN (
		SELECT tv_genres.name
		from tv_genres
			JOIN tv_show_genres ON (tv_genres.ID = tv_show_genres.genre_id)
			JOIN tv_shows ON(tv_shows.id = tv_show_genres.show_id)
		WHERE tv_shows.title = 'Dexter'
	)
ORDER BY tv_genres.name ASC;
