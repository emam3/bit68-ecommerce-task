from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from productApp.models import cartItem

@receiver(post_save, sender=cartItem)
def calculate_item_price(sender,created ,instance, **kwargs):
    if created:
        instance.itemPrice = instance.quantity * (instance.product.price)
        instance.save()