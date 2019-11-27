from django.shortcuts import render,HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Goods,Users
from .serializer import GoodsSerializer,UsersSerializer
from rest_framework import status
# Create your views here.


def index(request):
    return HttpResponse("hello word")


class GoodsAPI(APIView):
    renderer_classes =[JSONRenderer]
    # 查看
    def get(self,requset,*args,**kwargs):
        data = Goods.objects.all()
        print(type(data))
        #序列化
        goods = GoodsSerializer(data,many=True)
        print(goods.data)
        return Response({'msg':'data'})

    # 添加
    def post(self, request, *args, **kwargs):
        goods = GoodsSerializer(data=request.data)
        print(goods)
        # 验证
        if goods.is_valid():
            goods.save()
            return Response(goods.data,status=status.HTTP_200_OK)
        return Response(goods.errors,status=status.HTTP_400_BAD_REQUEST)

class GoodsIDAPI(APIView):
    # 修改
    def put(self,request,*args,**kwargs):
        goods = GoodsSerializer(data=request.data)
        print(goods)
        # 验证
        if goods.is_valid():
            goods.update(Goods.objects.filter(id = kwargs['id']).first(),request.data)
            return Response(goods.data, status=status.HTTP_200_OK)
        return Response(goods.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response({'msg':'ok'})
    # 删除
    def delete(self,rquest,*args,**kwargs):
        goods = Goods.objects.filter(id = kwargs['id']).first()
        if goods:
            goods.delete()
            return Response({'msg': 'ok'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# 用户

class UsersAPI(APIView):
    renderer_classes =[JSONRenderer]
    # 查看
    def get(self,requset,*args,**kwargs):
        data = Users.objects.all()
        print(type(data))
        #序列化
        users = UsersSerializer(data,many=True)
        print(users.data)
        return Response({'msg':'data'})

    # 添加
    def post(self, request, *args, **kwargs):
        users = UsersSerializer(data=request.data)
        print(users)
        # 验证
        if users.is_valid():
            users.save()
            return Response(users.data,status=status.HTTP_200_OK)
        return Response(users.errors,status=status.HTTP_400_BAD_REQUEST)

class UserIDAPI(APIView):
    # 修改
    def put(self,request,*args,**kwargs):
        users = UsersSerializer(data=request.data)
        print(users)
        # 验证
        if users.is_valid():
            users.update(Goods.objects.filter(id = kwargs['id']).first(),request.data)
            return Response(users.data, status=status.HTTP_200_OK)
        return Response(users.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response({'msg':'ok'})
    # 删除
    def delete(self,rquest,*args,**kwargs):
        users = Users.objects.filter(id = kwargs['id']).first()
        if users:
            users.delete()
            return Response({'msg': 'ok'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
