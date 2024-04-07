from django.db.models.signals import post_save
import datetime


def attention(sender, instance, created, **kwargs):
    if created and instance.creation_date == datetime.date.today():
        print(f"Сегодня премьера {instance.title}! 🥳")


post_save.connect(
    receiver=attention,
    sender="movies.Filmwork",
    weak=True,
    dispatch_uid="attention_signal",
)

# from django.dispatch import receiver

# @receiver(post_save, sender='movies.Filmwork')
# def attention(...):
