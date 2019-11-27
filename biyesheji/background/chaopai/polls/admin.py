from django.contrib import admin

# Register your models here.

from .models import Goods,Users,Shopcar,Goodsvalue,Order,Stock,Categoryproperties,Categroy,Categoryvalue
# verbose_name = u'数据管理'

@admin.register(Users)
class ChaopaiAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = "用户信息"
    list_display = ['username','password','name','reg_time','phone','real','birth','sex','address']





admin.site.register(Goods)
# admin.site.register(Users)
admin.site.register(Stock)
admin.site.register(Shopcar)
admin.site.register(Goodsvalue)
admin.site.register(Order)
admin.site.register(Categoryvalue)
admin.site.register(Categroy)
admin.site.register(Categoryproperties)


