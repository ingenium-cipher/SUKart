from django.contrib import admin
from .models import *

admin.site.register(ShoppingUser)
admin.site.register(DeliveryAgent)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Company)
admin.site.register(Product)
admin.site.register(ProductStatus)
admin.site.register(Category)


# Register your models here.
