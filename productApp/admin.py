from django.contrib import admin
from productApp.models import Product, cardItem, Card, checkOut


class productAdmin(admin.ModelAdmin):
    list_display = ["uuid", "title", "price"]

class cardItemAdmin(admin.ModelAdmin):
    list_display = ["uuid", "product", "quantity", "itemPrice"]

class CardAdmin(admin.ModelAdmin):
    list_display = ["uuid", "get_items"]

    def get_items(self,obj):
        try:
            return "\n".join([card.items for card in Card.objects.all()])
        except Exception as e:
            return []

class checkOutAdmin(admin.ModelAdmin):
    list_display = ["uuid"]

admin.site.register(Product, productAdmin)
admin.site.register(cardItem, cardItemAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(checkOut, checkOutAdmin)

# Register your models here.

