from django.db.models import Prefetch
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse

from .models import LookBook, FeaturesAds, Categories, SubCategories, BroadCategories, Goods


class HomePage(ListView):
    template_name = 'Goods/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        # context['title'] = 'Главная страница'
        context['lookbooks'] = LookBook.objects.filter(is_published=True)
        context['featuresads'] = FeaturesAds.objects.filter(is_published=True)
        context['categories'] = Categories.objects.all()
        context['subcategories'] = SubCategories.objects.all()
        context['broad_categories'] = BroadCategories.objects.all()
        return context

    def get_queryset(self):
        return "pass"


class ViewLookBook(DetailView):
    model = LookBook
    template_name = 'Goods/lookbook_detail.html'
    context_object_name = 'lookbook'


class ShowCategories(ListView):
    template_name = 'Goods/show_categories.html'
    queryset = "pass"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowCategories, self).get_context_data(**kwargs)
        context['broad_categories'] = BroadCategories.objects.prefetch_related('subcategories_set')
        context['categories'] = Categories.objects.prefetch_related('subcategories_set')
        return context


class ShowGoodsByBroadCategories(ListView):
    template_name = 'Goods/show_goods_by_broad_categories.html'
    context_object_name = 'subcategories_by_broad_categories'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowGoodsByBroadCategories, self).get_context_data(**kwargs)
        context['categories'] = Categories.objects.prefetch_related(
            Prefetch(
                "subcategories_set",
                queryset=SubCategories.objects.filter(slug__contains=f"{self.kwargs['broad_cat'].split('-')[-1]}")
            )
        )

        context['broad_categories'] = BroadCategories.objects.prefetch_related('subcategories_set')
        return context

    def get_queryset(self):
        return SubCategories.objects.filter(broad_category__slug=self.kwargs['broad_cat']).prefetch_related('goods_set')


class ShowGoodsBySubCat(ListView):
    template_name = 'Goods/show_goods_by_sub_cat.html'
    context_object_name = 'goods_by_subcategories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowGoodsBySubCat, self).get_context_data(**kwargs)
        context['broad_categories'] = BroadCategories.objects.prefetch_related('subcategories_set')
        context['categories'] = Categories.objects.prefetch_related(
            Prefetch(
                "subcategories_set",
                queryset=SubCategories.objects.filter(slug__contains=f"{self.kwargs['broad_cat'].split('-')[-1]}")
            )
        )

        return context

    def get_queryset(self):
        return Goods.objects.filter(sub_category__slug=self.kwargs['sub_cat'])


class GoodsInDetail(DetailView):
    model = Goods
    template_name = 'Goods/goods_in_detail.html'
    context_object_name = 'goods'

