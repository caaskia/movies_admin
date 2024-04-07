найти фильм, который был выпущен в прокат недалеко от важной для вас даты. 
Для этого вам нужно рассчитать расстояние между датами используя F, 
привести результат к количеству дней при помощи ExtractDay, 
избавиться от отрицательных значений при помощи Abs, 
отсортировать по получившемуся числу и взять первый фильм

filmwork_qs = Filmwork.objects.all()
expr = ExtractDay(models.ExpressionWrapper(
    datetime.datetime(2018, 11, 8 ) - F('creation_date'),
    output_field=models.DateField(),
))
film = filmwork_qs.annotate(delta=expr).filter(delta__isnull=False).annotate(abs_delta=Abs('delta')).order_by('abs_delta').first() 



