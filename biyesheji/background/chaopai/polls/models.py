from django.db import models

# Create your models here.
# 用户表
class Users(models.Model):
    class Meta:
        db_table = "users"
        verbose_name_plural='用户'
    username = models.CharField(max_length=20,verbose_name='用户名',default='admin')
    password = models.CharField(max_length=20,verbose_name='密码',default='admin')
    name = models.CharField(max_length=20,verbose_name='昵称',default='abc')
    reg_time = models.DateTimeField(auto_now=True,blank=True)
    phone = models.CharField(max_length=11,verbose_name='手机号')
    real = models.CharField(max_length=20,verbose_name='真实姓名',default='abc')
    birth = models.CharField(max_length=20,verbose_name='生日',default='1996-08-10')
    sex = models.CharField(max_length=20,verbose_name='性别',default='男')
    Provincial = models.ForeignKey('Provincial', on_delete=models.CASCADE, verbose_name="省")  # 省
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name="市")  # 市
    area = models.ForeignKey('Area', on_delete=models.CASCADE, verbose_name="区/县")  # 区
    address = models.CharField(max_length=100, verbose_name='地址')
    def __str__(self):
        return self.username
#
# 类目表
class Category(models.Model):
    class Meta:
        db_table = 'category'
        verbose_name = "类目"
        verbose_name_plural = "类目"
    name = models.CharField(max_length=20,verbose_name="类目名称")
    father = models.ForeignKey('self',db_index=False,on_delete=models.CASCADE,blank=True,null=True,verbose_name="父id")
    # def __str__(self):
    #     return self.name

# 类目规格表
class Attr(models.Model):
    class Meta:
        db_table = 'attr'
        verbose_name = "类目规格"
        verbose_name_plural = "类目规格"
    category = models.ForeignKey(to='Category',related_name= 'cate',on_delete=models.CASCADE,verbose_name="类目")
    name = models.CharField(max_length=20,verbose_name="规格名称")
    def __str__(self):
        return self.name


# 类目规格选项表
class AttrChoice(models.Model):
    class Meta:
        db_table = 'attrchoice'
        verbose_name = "类目规格选项"
        verbose_name_plural = "类目规格选项"
    attr = models.ForeignKey(to='Attr',related_name='attr',on_delete=models.CASCADE,verbose_name="类目规格")
    color = models.CharField(max_length=20,verbose_name="规格选项颜色")
    size = models.CharField(max_length=20, verbose_name="规格选项尺寸")
    # def __str__(self):
    #     return self.name

# 商品表
class Goods(models.Model):
    class Meta:
        db_table = 'goods'
        verbose_name = "商品管理"
        verbose_name_plural = "商品管理"
    name = models.CharField(max_length=20,verbose_name="商品名称")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="类目")
    info = models.CharField(max_length=200,verbose_name="商品简介")
    goods_id =models.CharField(max_length=10,verbose_name="商品编码")
    img = models.ImageField(upload_to="goods",verbose_name="商品图片")
    price = models.CharField(max_length=20, verbose_name='价格')
    def __str__(self):
        return self.name


# 库存规格关联表
class ExhaustedAttr(models.Model):
    exhausted = models.ForeignKey("Exhausted", on_delete=models.CASCADE)
    attr = models.ForeignKey(Attr, on_delete=models.CASCADE)
    attrchoice = models.ForeignKey(AttrChoice,on_delete=models.CASCADE,verbose_name="规格选项")

# 库存表
class Exhausted(models.Model):
    class Meta:
        db_table = 'exhausted'
        verbose_name = "库存管理"
        verbose_name_plural = "库存管理"
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name="商品")
    attr = models.ManyToManyField(Attr,through=ExhaustedAttr)
    num = models.IntegerField(verbose_name='数量')

    def __str__(self):
        return self.num

# 购物车表
class Shopcar(models.Model):
    class Meta:
        db_table = 'shopcar'
        verbose_name = '购物车'
        verbose_name_plural = '购物车'
    gid = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name='商品id')
    uid = models.ForeignKey(Users,on_delete=models.CASCADE,verbose_name='用户id')
    num = models.IntegerField(default=0,verbose_name="购买数量")


# 订单关联表
class OrderAttr(models.Model):
    exhausted = models.ForeignKey(Exhausted,on_delete=models.CASCADE)  # 库存
    order = models.ForeignKey('Order',on_delete=models.CASCADE)  # 订单


# 订单表
class Order(models.Model):
    class Meta:
        db_table = 'order'
        verbose_name = '订单表'
        verbose_name_plural = '订单表'
    exhausted = models.ManyToManyField(Exhausted,through=OrderAttr)
    orders = models.CharField(max_length=20,verbose_name='订单号')
    gid = models.ForeignKey(Goods,on_delete=models.CASCADE)
    uid = models.ForeignKey(Users, on_delete=models.CASCADE,verbose_name='用户')
    status = models.ForeignKey("Status",on_delete=models.CASCADE,verbose_name='状态')
    pay = models.ForeignKey('Pay',on_delete=models.CASCADE,verbose_name='支付方式')
    time = models.DateTimeField(auto_now=True,blank=True,verbose_name='下单时间')

class Status(models.Model):
    class Meta:
        db_table = 'status'
        verbose_name = '状态表'
        verbose_name_plural = '状态表'
    status = models.CharField(max_length=20,verbose_name='状态')
    def __str__(self):
        return self.status

class Pay(models.Model):
    class Meta:
        db_table = 'pay'
        verbose_name = '支付方式表'
        verbose_name_plural = '支付方式表'
    pay = models.CharField(max_length=20,verbose_name='支付方式')
    def __str__(self):
        return self.pay
# 详情表
class Page(models.Model):
    class Meta:
        db_table = 'page'
        verbose_name = '详情表'
        verbose_name_plural = '详情表'
    # goods = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name='商品')
    exhausted = models.ForeignKey(Exhausted, on_delete=models.CASCADE)  # 库存
    # attr = models.ForeignKey(Attr,on_delete=models.CASCADE,null=True)
    # AttrChoice = models.ForeignKey(AttrChoice,on_delete=models.CASCADE)

#
# # 类目
# class Category(models.Model):
#     class Meta:
#         db_table = "category"
#         verbose_name_plural = '类目表'
#     name = models.CharField(max_length=20, verbose_name='类名')
#     def __str__(self):
#         return self.name
#
#
# # 类目属性表
# class Categoryproperties(models.Model):
#     class Meta:  # 元类
#         db_table = "categoryproperties"
#         verbose_name_plural = '类目属性表'
#     cid = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='类名')
#     name = models.CharField(max_length=200,verbose_name='类目属性名')
#     def __str__(self):
#         return self.name
# # 类目属性值
# class Categoryvalue(models.Model):
#     class Meta:
#         db_table = "categoryvalue"
#         verbose_name_plural = '类目属性值表'
#     cid = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='类目id')
#     cpid = models.ForeignKey(Categoryproperties,on_delete=models.CASCADE,verbose_name="类目属性名")
#     name = models.CharField(max_length=20, verbose_name='类目属性值名')
#     def __str__(self):
#         return self.name
#
# # 商品表
# class Goods(models.Model):
#     class Meta:  # 元类
#         db_table = "goods"
#         verbose_name_plural = '商品表'
#     cid = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='类目id')
#     name = models.CharField(max_length=20,verbose_name='商品名')
#     describe = models.CharField(max_length=200,verbose_name="描述")
#     img = models.CharField(max_length=200,verbose_name='图片')
#     style = models.CharField(max_length=20,verbose_name='样式')
#     time = models.DateTimeField(auto_now=True,blank=True,verbose_name='时间')
#     color = models.CharField(max_length=20, verbose_name='颜色')
#     size = models.CharField(max_length=20, verbose_name='尺码')
#     price = models.CharField(max_length=20, verbose_name='价格')
#     num = models.IntegerField(verbose_name='数量')
#     def __str__(self):
#         return self.name
# # 商品属性值表
# class Goodsvalue(models.Model):
#     class Meta:
#         db_table = "goodsvalue"
#         verbose_name_plural = '商品属性表'
#     # gid = models.IntegerField(verbose_name='商品id')
#     gid = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name='商品id')
#     color = models.CharField(max_length=20,verbose_name='颜色')
#     size = models.CharField(max_length=20, verbose_name='尺码')
#     price = models.CharField(max_length=20, verbose_name='价格')
#     num = models.IntegerField( verbose_name='数量')
#
# # 库存
# class Stock(models.Model):
#     class Meta:
#         db_table = 'stock'
#         verbose_name_plural = '库存表'
#     # goods = models.IntegerField(verbose_name='商品id')
#     gid = models.ForeignKey(Goods, on_delete=models.CASCADE,verbose_name='商品id')
#     stock = models.CharField(max_length=20, verbose_name='库存')
#     def __str__(self):
#         return self.stock
# # 购物车
# class Shopcar(models.Model):
#     class Meta:  # 元类
#         db_table = "shopcar"
#         verbose_name_plural = '购物车'
#     # gid = models.IntegerField(verbose_name='商品id')
#     # uid = models.IntegerField(verbose_name='用户id')
#     gid = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name='商品id')
#     uid = models.ForeignKey(Users,on_delete=models.CASCADE,verbose_name='用户id')
#     total = models.IntegerField(verbose_name='数量')
# # 订单表
# class Order(models.Model):
#     class Meta:
#         db_table = "order"
#         verbose_name_plural = '订单表'
#     orders = models.CharField(max_length=20,verbose_name='订单号')
#     uid = models.ForeignKey(Users, on_delete=models.CASCADE,verbose_name='用户')
#     gid = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name='商品id')
#     status = models.CharField(max_length=20,verbose_name='状态')
#     pay = models.CharField(max_length=20,verbose_name='支付方式')
#     time = models.DateTimeField(auto_now=True,blank=True,verbose_name='下单时间')
# 省
class Provincial(models.Model):
    class Meta:
        db_table = "provinces"
    provinceid = models.IntegerField(verbose_name="省编码",unique=True)
    province = models.CharField(max_length=100, verbose_name="省")
    def __str__(self):
        return self.province
# 市
class City(models.Model):
    class Meta:
        db_table ="cities"
    cityid = models.CharField(max_length=6, verbose_name="城市编码",unique=True)
    city = models.CharField(max_length=40, verbose_name="城市名称")
    provinceid = models.ForeignKey(Provincial,to_field="provinceid",on_delete=models.CASCADE)
    def __str__(self):
        return self.city
# 区县
class Area(models.Model):
    class Meta:
        db_table = "areas"
    areaid = models.CharField(max_length=6,verbose_name="区县编码")
    area = models.CharField(max_length=40,verbose_name="区县名称")
    cityid = models.ForeignKey(City,to_field="cityid",on_delete=models.CASCADE)
    def __str__(self):
        return self.area



