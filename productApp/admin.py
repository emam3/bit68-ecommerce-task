from django.contrib import admin
from productApp.models import Product, cartItem, Cart, checkOut


class productAdmin(admin.ModelAdmin):
    list_display = ["uuid", "title", "price"]

class cartItemAdmin(admin.ModelAdmin):
    list_display = ["uuid", "product", "quantity", "itemPrice"]

class cartAdmin(admin.ModelAdmin):
    list_display = ["uuid", "get_items"]

    def get_items(self,obj):
        try:
            return "\n".join([cart.items for cart in Cart.objects.all()])
        except Exception as e:
            return []

class checkOutAdmin(admin.ModelAdmin):
    list_display = ["uuid"]

admin.site.register(Product, productAdmin)
admin.site.register(cartItem, cartItemAdmin)
admin.site.register(Cart, cartAdmin)
admin.site.register(checkOut, checkOutAdmin)

# Register your models here.

