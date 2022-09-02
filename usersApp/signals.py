from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from productApp.models import Card
from usersApp.models import User

@receiver(post_save, sender=User)
def create_user_card(sender, instance, created, **kwargs):
    if created:
        new_card = Card.objects.create()
        instance.card = new_card
        instance.save()