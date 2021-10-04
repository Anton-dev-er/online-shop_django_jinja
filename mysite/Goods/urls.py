from django.urls import path

from .views import HomePage, ViewLookBook

urlpatterns = [
    path('main-page', HomePage.as_view(), name='main_page'),
    path('lookbook/<int:pk>', ViewLookBook.as_view(), name='view_lookbook'),
]