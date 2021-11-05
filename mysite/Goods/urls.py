from django.urls import path

from .views import *

urlpatterns = [
    path('home', HomePage.as_view(), name='home'),
    path('home/lookbook/<int:pk>', ViewLookBook.as_view(), name='view_lookbook'),
    path('catalog', ShowCategories.as_view(), name='show_categories'),
    path('catalog/<slug:broad_cat>', ShowGoodsByBroadCategories.as_view(), name='show_goods_by_broad_categories'),
    path('catalog/<slug:broad_cat>/<slug:sub_cat>', ShowGoodsBySubCat.as_view(), name='show_goods_by_sub_cat'),
    path('home/<slug:slug>', GoodsInDetail.as_view(), name='goods_in_detail'),
]