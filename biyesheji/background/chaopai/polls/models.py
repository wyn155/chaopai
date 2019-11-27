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
    address = models.CharField(max_length=100, verbose_name='地址',default='太原')
# 类目
class Categroy(models.Model):
    class Meta:
        db_table = "category"
        verbose_name_plural = '类目表'
    name = models.CharField(max_length=20, verbose_name='类名')
    def __str__(self):
        return self.name


# 类目属性表
class Categoryproperties(models.Model):
    class Meta:  # 元类
        db_table = "categoryproperties"
        verbose_name_plural = '类目属性表'
    cid = models.ForeignKey(Categroy,on_delete=models.CASCADE,verbose_name='类名')
    name = models.CharField(max_length=200,verbose_name='类目属性名')
    def __str__(self):
        return self.name
# 类目属性值
class Categoryvalue(models.Model):
    class Meta:
        db_table = "categoryvalue"
        verbose_name_plural = '类目属性值表'
    cid = models.ForeignKey(Categroy,on_delete=models.CASCADE,verbose_name='类目id')
    name = models.CharField(max_length=20, verbose_name='类目属性值名')
    def __str__(self):
        return self.name

# 商品表
class Goods(models.Model):
    class Meta:  # 元类
        db_table = "goods"
        verbose_name_plural = '商品表'
    cid = models.ForeignKey(Categroy,on_delete=models.CASCADE,verbose_name='类目id')
    name = models.CharField(max_length=20,verbose_name='商品名')
    describe = models.CharField(max_length=200,verbose_name="描述")
    img = models.CharField(max_length=200,verbose_name='图片')
    style = models.CharField(max_length=20,verbose_name='样式')
    time = models.DateTimeField(auto_now=True,blank=True)
# 商品属性值表
class Goodsvalue(models.Model):
    class Meta:
        db_table = "goodsvalue"
        verbose_name_plural = '商品属性表'
    # gid = models.IntegerField(verbose_name='商品id')
    gid = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name='商品id')
    color = models.CharField(max_length=20,verbose_name='颜色')
    size = models.CharField(max_length=20, verbose_name='尺码')
    price = models.CharField(max_length=20, verbose_name='价格')
    num = models.IntegerField( verbose_name='数量')


# 库存
class Stock(models.Model):
    class Meta:
        db_table = 'stock'
        verbose_name_plural = '库存表'
    # goods = models.IntegerField(verbose_name='商品id')
    gid = models.ForeignKey(Goods, on_delete=models.CASCADE,verbose_name='商品id')
    stock = models.CharField(max_length=20, verbose_name='库存')
    def __str__(self):
        return self.stock
# 购物车
class Shopcar(models.Model):
    class Meta:  # 元类
        db_table = "shopcar"
        verbose_name_plural = '购物车'
    # gid = models.IntegerField(verbose_name='商品id')
    # uid = models.IntegerField(verbose_name='用户id')
    gid = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name='商品id')
    uid = models.ForeignKey(Users,on_delete=models.CASCADE,verbose_name='用户id')
    total = models.CharField(max_length=20,verbose_name='总价')
# 订单表
class Order(models.Model):
    class Meta:
        db_table = "order"
        verbose_name_plural = '订单表'
    orders = models.CharField(max_length=20,verbose_name='订单号')
    uid = models.ForeignKey(Users, on_delete=models.CASCADE,verbose_name='用户')
    # uid = models.IntegerField(verbose_name='用户id')
    status = models.CharField(max_length=20,verbose_name='状态')
    pay = models.CharField(max_length=20,verbose_name='支付方式')
    time = models.DateTimeField(auto_now=True,blank=True)



