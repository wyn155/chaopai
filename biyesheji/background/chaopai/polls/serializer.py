from rest_framework.serializers import ModelSerializer,DateTimeField
from .models import Goods,Users,Shopcar,Order,Page,Attr,AttrChoice,Exhausted,Category
from rest_framework import serializers
# 商品
class GoodsSerializer(ModelSerializer):
    time = DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    class Meta:
        model = Goods
        fields =['category','name','info','img','time','price']
# 用户
class UsersSerializer(ModelSerializer):
    reg_time = DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    class Meta:
        model = Users
        fields =['username','password','name','phone','reg_time','real','birth','sex','address']
# 购物车
class ShopcarSerializer(ModelSerializer):

    class Meta:
        model = Shopcar
        fields =['id','uid','gid']

class AttrSerializer(ModelSerializer):

    class Meta:
        model = Attr
        fields =['id','category','name']

class AttrchoiceSerializer(ModelSerializer):

    class Meta:
        model = AttrChoice
        fields =['id','attr','size','color']
# class ShopcarSerializer(serializers.Serializer):
#     user = serializers.HiddenField(
#         default=serializers.CurrentUserDefault()
#     )
#     num = serializers.IntegerField(required=True,min_value=1
#         #                            error_messages={
#         # "min_value":'商品数量不能小于1',
#         # 'required':'亲选择购买数量'
#     # }
#     )
#     goods = serializers.PrimaryKeyRelatedField(required=True,queryset=Goods.objects.all())
#     def create(self, validated_data):
#         user = self.context['request'].user
#         num = validated_data['num']
#         goods = validated_data['goods']
#
#         existed = Shopcar.objects.filter(user=user,goods = goods)
#         if existed:
#             existed = existed[0]
#             existed.num+=num
#             existed.save()
#         else:
#             existed = Shopcar.objects.create(**validated_data)
#         return existed
# 库存
# class ExhaustedSerializer(ModelSerializer):
#     class Meta:
#         model = Exhausted
#         fields = ['goods','num']
# 订单
class OrderSerializer(ModelSerializer):
    time = DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    class Meta:
        model = Order
        fields = ['orders','gid','uid','status','pay','time']

        def generate_order_sn(self):  # 订单号
            # 当前时间+userid+随机数
            from random import Random
            import time
            random_ins = Random()
            order_sn = "{time_str}{userid}{ranstr}".format(time_str=time.strftime("%Y%m%d%H%M%S"),
                                                           userid=self.context['request'].user.id,
                                                           ranstr=random_ins.randint(10, 99))
            return order_sn

        def validate(self, attrs):  # 添加订单号
            attrs['orders'] = self.generate_order_sn()
            return attrs
# 详情
class PageSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = ['id','exhausted',]
# 详情
# class OrderSerializer(ModelSerializer):
#     class Meta:
#         model = Order
#         fields = ['attrs','uid','status','pay','gid']
#         def generate_order_sn(self):  # 订单号
#             # 当前时间+userid+随机数
#             from random import Random
#             import time
#             random_ins = Random()
#             order_sn = "{time_str}{userid}{ranstr}".format(time_str=time.strftime("%Y%m%d%H%M%S"),
#                                                            userid=self.context['request'].user.id,
#                                                            ranstr=random_ins.randint(10, 99))
#             return order_sn
#
#         def validate(self, attrs):  # 添加订单号
#             attrs['orders'] = self.generate_order_sn()
#             return attrs