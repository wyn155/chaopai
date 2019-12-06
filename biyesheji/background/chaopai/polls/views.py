from django.shortcuts import render,HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Goods,Users,Category,Shopcar,Order,Page,Attr,AttrChoice,Exhausted,Status,Pay
from .serializer import GoodsSerializer,UsersSerializer,ShopcarSerializer,OrderSerializer,PageSerializer,AttrSerializer,AttrchoiceSerializer
from rest_framework import status,mixins
from django.core import serializers
# Create your views here.
from rest_framework import viewsets

def index(request):
    return HttpResponse("hello word")


class GoodsAPI(APIView):
    renderer_classes =[JSONRenderer]
    # 查看
    def get(self,requset,*args,**kwargs):
        data = Goods.objects.all()
        #序列化
        goods = GoodsSerializer(data,many=True)

        categroy = Category.objects.get(id = goods.data[0]['category'])
        goods.data[0]['category'] = categroy.name
        # goods = goods.update(name=data)
        # print(goods)
        return Response({'msg':goods.data})

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
        return Response({'msg':users.data})

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

class ShopcarAPI(APIView):
    renderer_classes = [JSONRenderer]
    def get(self,request,*args,**kwargs):
        data = Shopcar.objects.all()
        data = ShopcarSerializer(data, many=True)
        # print(type(data))
        goods = Goods.objects.filter(id=data.data[0]['gid'])
        for goods in goods:
            name = goods.name
            img = goods.img
            print(img)
            describe = goods.info
            price = goods.price
            data = {'name':name,'img':img,'price':price,'describe':describe}
            print(goods.category.id)
            attr = Attr.objects.all()
            category = Category.objects.filter(id = goods.category.id).first()
            category = category.cate.all()
            for i in category:
                pk = i.id
                attr = Attr.objects.filter(id=pk).first()
                attr = attr.attr.all()
                import json
                item = serializers.serialize("json", attr)
                item = json.loads(item)
                for item in item:
                    # print(item['model'])
                    # print(item['fields'])
                    # print(item['fields']['attr'])
                    color = item['fields']['color']
                    size = item['fields']['size']
                    con = {'color': color, 'size': size}
            # print(data)
            dict1 = dict(data,**con)
            print(dict1)
        return Response({'msg': 'dict1'})
class ShopIDAPI(APIView):
    def delete(self, rquest, *args, **kwargs):
        shopcar = Shopcar.objects.filter(id=kwargs['id']).first()
        if shopcar:
            shopcar.delete()
            return Response({'msg': 'ok'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class PageAPI(APIView):
    renderer_classes = [JSONRenderer]
    def get(self, request, *args, **kwargs):
        data = Page.objects.all()
        page = PageSerializer(data, many=True)
        exhausted = Exhausted.objects.filter(id=page.data[0]['exhausted'])
        item = serializers.serialize("json", exhausted)
        import json
        item = json.loads(item)
        for item in item:
            num = item['fields']['num']
            num = {'num':num}
            goods = item['fields']['goods']
            goods = Goods.objects.filter(id=goods)
            for goods in goods:
                name = goods.name
                img = goods.img
                print(img)
                describe = goods.info
                price = goods.price
                data = {'name': name, 'img': img, 'price': price, 'describe': describe}
                data = dict(num,**data)
                print(data)
                print(goods.category.id)
                attr = Attr.objects.all()
                category = Category.objects.filter(id=goods.category.id).first()
                category = category.cate.all()
                for i in category:
                    pk = i.id
                    attr = Attr.objects.filter(id=pk).first()
                    attr = attr.attr.all()
                    import json
                    item = serializers.serialize("json", attr)
                    item = json.loads(item)
                    for item in item:
                        # print(item['model'])
                        # print(item['fields'])
                        # print(item['fields']['attr'])
                        color = item['fields']['color']
                        size = item['fields']['size']
                        con = {'color': color, 'size': size}
                        dict2 = dict(data,**con)
                print(dict2)
        print(page)
        return Response({'msg': 'dict2'})
class OrderAPI(APIView):
    renderer_classes = [JSONRenderer]
    # 查看
    def get(self, requset, *args, **kwargs):
        data = Order.objects.all()
        print(data)
        # 序列化
        order = OrderSerializer(data, many=True)
        print(order)
        # for item in order:
        #     goods = item.gid
        #     users = item.uid
        #     pay = item.pay
        #     status = item.status
        #     orders = item.orders
        #     dict3 = {'users':users,'pay':pay,'status':status,'orders':orders}
        #     print(dict3)
        # print(order)
        # goods = Goods.objects.filter(id=order.data[2]['gid'])
        # status = Status.objects.get(id = order.data[]['status'])
        # print(status)
        # print(goods)
        # order.data[2]['gid'] = goods.name
        return Response({'msg':order.data})

    # 添加
    def post(self, request, *args, **kwargs):
        order = OrderSerializer(data=request.data)
        print(order)
        # 验证
        if order.is_valid():
            order.save()
            return Response(order.data, status=status.HTTP_200_OK)
        return Response(order.errors, status=status.HTTP_400_BAD_REQUEST)

