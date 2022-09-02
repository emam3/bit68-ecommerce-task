from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from productApp.models import Cart
from usersApp.models import User

@receiver(post_save, sender=User)
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        new_cart = Cart.objects.create()
        instance.cart = new_cart
        instance.save()