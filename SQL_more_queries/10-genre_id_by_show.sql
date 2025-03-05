-- This script selects the title of TV shows and their genre IDs from the hbtn_0d_tvshows database.
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows
INNER JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id 
ORDER BY tv_shows.title, tv_show_genres.genre_id;