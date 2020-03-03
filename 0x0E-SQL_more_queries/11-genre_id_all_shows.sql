-- > This script lists all shows contained in the database hbtn_0d_tvshows.
-- > If a show has no genre, display NULL.

SELECT title, genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY title ASC, genre_id ASC;
