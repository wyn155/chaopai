from django.contrib import admin

# Register your models here.

from .models import Goods,Users,Shopcar,Order,Category,Pay,Status,AttrChoice,Attr,Exhausted,ExhaustedAttr,OrderAttr,Page
# # verbose_name = u'数据管理'
#
from django.contrib import admin
# from .models import Category,Attr,AttrChoice,Goods,Exhausted,ExhaustedAttr,Users,Shopcar,Order,Pay,Status,OrderAttr,Page
from django.utils.html import format_html

@admin.register(Users)
class ChaopaiAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = "用户信息"
    list_display = ['username','password','name','phone','real','birth','sex','Provincial','city','area','address']
    fieldsets = (
        ("账号管理",{
            'fields':('username','password')
        }),
        ("个人信息", {
            'fields': ('name', 'real','phone')
        }),
        ('收货地址', {
            'fields': ('Provincial', 'city', 'area', 'address')
        })
    )

def get_con(obj):
    if obj.father == None:
        return obj.name
    return obj.name +"<"+ get_con(Category.objects.filter(id=obj.father_id).first())


# Register your models here.
from .models import Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','get_name','get_father')
    def get_father(self,obj):
        return str(obj.father_id)
    def get_name(self,obj):
        return get_con(obj)

@admin.register(Attr)
class AttrAdmin(admin.ModelAdmin):
    list_display = ('id','name','category')

@admin.register(AttrChoice)
class AttrChoiceAdmin(admin.ModelAdmin):
    list_display = ('id','size','attr','color')

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id','get_img','category','name','info')
    def get_img(self,obj):
        return format_html("<img src='/static/%s' height='50' >"%obj.img)

class AttrInline(admin.TabularInline):
    model = ExhaustedAttr



# 库存
@admin.register(Exhausted)
class ExhaustedAdmin(admin.ModelAdmin):
    inlines = [
        AttrInline,
    ]
    list_display = ('goods',"get_attr",'num')
    def get_attr(self,obj):
        str1 = ""
        for item in obj.exhaustedattr_set.filter(exhausted=obj.id):
            str1+="%s:%s  、 "%(item.attr,item.attrchoice)
        return str1
class AttrInlines(admin.TabularInline):
    model = OrderAttr
# 订单
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        AttrInlines,
    ]
    list_display = ('id','get_exhausted','orders','uid','status','pay')
    def get_exhausted(self,obj):
        str1 = ''
        for item in obj.orderattr_set.filter(order=obj.id):
            str1+=item.exhausted
        return str1

    # def generate_order_sn(self):  # 订单号
    #     # 当前时间+userid+随机数
    #     from random import Random
    #     import time
    #     random_ins = Random()
    #     order_sn = "{time_str}{userid}{ranstr}".format(time_str=time.strftime("%Y%m%d%H%M%S"),
    #                                                    userid=self.context['request'].user.id,
    #                                                    ranstr=random_ins.randint(10, 99))
    #     return order_sn
    # # def validate(self, attrs):  # 添加订单号
    # #     attrs['orders'] = self.generate_order_sn()
    # #     return attrs
# 详情表
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('id','exhausted')


# 支付方式
@admin.register(Pay)
class PayAdmin(admin.ModelAdmin):
    list_display = ('pay',)

# 状态
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('status',)





#
# @admin.register(Category)
# class ChaopaiAdmin(admin.ModelAdmin):
#     class Meta:
#         verbose_name_plural = "类目表"
#     list_display = ['name']
# @admin.register(Categoryproperties)
# class ChaopaiAdmin(admin.ModelAdmin):
#     class Meta:
#         verbose_name_plural = "类目属性表"
#     list_display = ['cid','name']
#
# @admin.register(Categoryvalue)
# class ChaopaiAdmin(admin.ModelAdmin):
#     class Meta:
#         verbose_name_plural = "类目属性值表"
#     list_display = ['cid','cpid','name']
# @admin.register(Goods)
# class ChaopaiAdmin(admin.ModelAdmin):
#     class Meta:
#         verbose_name_plural = "商品表"
#     list_display = ['id','cid','name','describe','img','style','time']
#
# # @admin.register(Goodsvalue)
# # class ChaopaiAdmin(admin.ModelAdmin):
# #     class Meta:
# #         verbose_name_plural = "商品属性表"
# #     list_display = ['gid','color','size','price','num']
#
# @admin.register(Stock)
# class ChaopaiAdmin(admin.ModelAdmin):
#     class Meta:
#         verbose_name_plural = "库存表"
#     list_display = ['gid','stock']
# @admin.register(Shopcar)
# class ChaopaiAdmin(admin.ModelAdmin):
#     class Meta:
#         verbose_name_plural = "购物车表"
#     list_display = ['gid','uid','total']
#
# @admin.register(Order)
# class ChaopaiAdmin(admin.ModelAdmin):
#     class Meta:
#         verbose_name_plural = "订单表"
#     list_display = ['uid','gid','orders','status','pay','time']
#
#


