from django.contrib import admin

# Register your models here.
from .models import Post

admin.site.site_header = 'Kilobiryani administration'

@admin.register(Post)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','offer')
    actions = ['discount_30','discount_20','remove_offer']

    def remove_offer(self, request, queryset):
        for product in queryset:
            product.offer = 0
            product.save(update_fields=['offer'])
    remove_offer.short_description = 'Remove offer'

    def discount_30(self, request, queryset):
        from math import ceil
        discount = 30  # percentage

        for product in queryset:
            """ Set a discount of 30% to selected products """
            multiplier = discount / 100.  # discount / 100 in python 3
            old_price = product.price
            new_price = ceil(old_price - (old_price * multiplier))
            product.offer = new_price
            product.save(update_fields=['offer'])
    discount_30.short_description = 'Set 30%% discount'


    def discount_20(self, request, queryset):
        from math import ceil
        discount = 20  # percentage

        for product in queryset:
            """ Set a discount of 20% to selected products """
            multiplier = discount / 100.  # discount / 100 in python 3
            old_price = product.price
            new_price = ceil(old_price - (old_price * multiplier))
            product.offer = new_price
            product.save(update_fields=['offer'])
    discount_20.short_description = 'Set 20%% discount'