films = FilmWork.objects.filter(filmwork__role=PersonFilmWork.RoleChoices.ACTOR)


SELECT "content"."film_work"."id",
       "content"."film_work"."created",
       "content"."film_work"."modified",
       "content"."film_work"."title",
       "content"."film_work"."description",
       "content"."film_work"."creation_date",
       "content"."film_work"."rating",
       "content"."film_work"."type",
       "content"."film_work"."certificate",
       "content"."film_work"."file_path"
FROM   "content"."film_work"
       INNER JOIN "content"."person_film_work"
               ON ( "content"."film_work"."id" =
                    "content"."person_film_work"."film_work_id" )
WHERE  "content"."person_film_work"."role" = actor 
