-- This script selects the title of TV shows that do not have any genre assigned.
SELECT tvs.title, NULL AS genre_id
FROM tv_shows tvs
LEFT JOIN tv_show_genres tvsg ON tvs.id = tvsg.show_id
WHERE tvsg.genre_id IS NULL
ORDER BY tvs.title;