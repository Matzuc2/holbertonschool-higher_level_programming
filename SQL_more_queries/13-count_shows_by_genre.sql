-- This script counts the number of TV shows by genre from the hbtn_0d_tvshows database.
SELECT tv_genres.name AS 'genre', COUNT(*) AS 'number_of_shows'
FROM tv_genres 
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;