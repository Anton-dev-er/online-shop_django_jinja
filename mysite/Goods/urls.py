from django.urls import path

from .views import HomePage, ViewLookBook

urlpatterns = [
    path('home', HomePage.as_view(), name='Home'),
    path('lookbook/<int:pk>', ViewLookBook.as_view(), name='view_lookbook'),
]