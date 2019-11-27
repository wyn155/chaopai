from django.urls import path
from . import views
from .views import GoodsAPI,GoodsIDAPI,UserIDAPI,UsersAPI
urlpatterns = [
    path('',views.index,name='index'),
    path('api/goods',GoodsAPI.as_view()),
    path('api/goods/<int:id>',GoodsIDAPI.as_view()),
    path('api/users', UsersAPI.as_view()),
    path('api/users/<int:id>', UserIDAPI.as_view()),
]