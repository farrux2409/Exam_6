from django.contrib import admin

from blog.models import Product,  Image, Attribute,Customer

# Register your models here.


admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Attribute)
admin.site.register(Customer)
#admin.site.register(admin.CustomerAdmin)
'''
@admin.register(Customer)
class Customer(admin.ModelAdmin):
    List_display = ("name", "email", "phone", "billing_address", " joined_date")
    
    List_filter = ("Customer")
'''
    

