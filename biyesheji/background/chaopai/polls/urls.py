from django.urls import path
from . import views
from .views import GoodsAPI,GoodsIDAPI,UserIDAPI,UsersAPI,ShopcarAPI,ShopIDAPI,OrderAPI,PageAPI
urlpatterns = [
    path('',views.index,name='index'),
    path('api/goods',GoodsAPI.as_view()),
    path('api/goods/<int:id>',GoodsIDAPI.as_view()),
    path('api/users', UsersAPI.as_view()),
    path('api/users/<int:id>', UserIDAPI.as_view()),
    path('api/shopcar',ShopcarAPI.as_view()),
    path('api/shopcar/<int:id>',ShopIDAPI.as_view()),
    path('api/page',PageAPI.as_view()),
    path('api/order',OrderAPI.as_view()),
    path('api/order/<int:id>',OrderAPI.as_view()),
]