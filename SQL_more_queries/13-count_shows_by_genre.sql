-- This script counts the number of TV shows by genre from the hbtn_0d_tvshows database.
SELECT tv_genres.name as genre, COUNT(*) AS number_of_shows
FROM tv_show_genres JOIN tv_shows ON tv_show_genres.genre_id = tv_shows.id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;