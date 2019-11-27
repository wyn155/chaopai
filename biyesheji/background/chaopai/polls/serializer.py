from rest_framework.serializers import ModelSerializer,DateTimeField
from .models import Goods,Users

class GoodsSerializer(ModelSerializer):
    time = DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    class Meta:
        model = Goods
        fields =['name','describe','img','style','time']

class UsersSerializer(ModelSerializer):
    reg_time = DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    class Meta:
        model = Users
        fields =['username','password','name','phone','reg_time','real','birth','sex','address']