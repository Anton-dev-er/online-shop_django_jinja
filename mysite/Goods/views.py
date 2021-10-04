from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from django.http import HttpResponse

from .models import LookBook, FeaturesAds


class HomePage(ListView):
    template_name = 'Goods/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['lookbooks'] = LookBook.objects.filter(is_published=True)
        context['featuresads'] = FeaturesAds.objects.filter(is_published=True)
        return context

    def get_queryset(self):
        return '123'


class ViewLookBook(DeleteView):
    model = LookBook
    template_name = 'Goods/lookbook_detail.html'
    context_object_name = 'lookbook'


