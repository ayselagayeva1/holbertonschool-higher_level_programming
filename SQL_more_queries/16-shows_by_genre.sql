-- Bu script hbtn_0d_tvshows bazasındakı bütün şouları və onlara aid janrları siyahıya alır
-- Əgər şouya janr təyin edilməyibsə, NULL göstərilir
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
