-- This script counts the number of TV shows by genre from the hbtn_0d_tvshows database.
USE hbtn_0d_tvshows;

SELECT tv_genres.name as genre, COUNT(*) as number_of_shows
FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.genre_id = tv_shows.id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_shows.id
ORDER BY number_of_shows DESC;