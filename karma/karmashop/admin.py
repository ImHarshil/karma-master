from django.contrib import admin
from core import models as core_models

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id' , "user_id", 'mobile_number','alternate_mobile_number']

class AddressAdmin(admin.ModelAdmin):
    list_display = ['id','address_line1','address_line2','city','state','country','zipcode']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','discription','quantity','category','img']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','user','transection_id','is_completed','created_date']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id','product','order','quantity','created_date']

class ShippingInfoAdmin(admin.ModelAdmin):
    list_display = ['id','user','order','address','created_date']


admin.site.register(core_models.Profile,ProfileAdmin)
admin.site.register(core_models.Address,AddressAdmin)
admin.site.register(core_models.Product,ProductAdmin)
admin.site.register(core_models.Order, OrderAdmin)
admin.site.register(core_models.OrderItem,OrderItemAdmin)
admin.site.register(core_models.ShippingInfo,ShippingInfoAdmin)






