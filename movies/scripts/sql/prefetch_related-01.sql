actors = Person.objects.filter(
        personfilmwork__role=PersonFilmWork.RoleChoices.ACTOR
    ).prefetch_related("personfilmwork__film_work")
    
SELECT "content"."person"."id",
       "content"."person"."created",
       "content"."person"."modified",
       "content"."person"."full_name"
FROM   "content"."person"
       INNER JOIN "content"."person_film_work"
               ON ( "content"."person"."id" =
                  "content"."person_film_work"."person_id" )
WHERE  "content"."person_film_work"."role" = actor 
