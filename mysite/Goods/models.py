from django.db import models as m
from slugify import slugify
from django.urls import reverse


#
#
# class Goods(m.Model):
#     title = m.CharField(max_length=50)
#     small_description = m.CharField(max_length=50)
#     description = m.TextField()
#     price = m.IntegerField()
#     photo = m.ImageField(upload_to="photos/%Y/%m/%d/")
#     size = m.CharField(max_length=5)
#     is_sale = m.BooleanField(default=False)
#     selling_price = m.IntegerField()
#     description_sale = m.TextField(blank=True)
#     created_dt = m.DateTimeField(auto_now_add=True)
#     updated_dt = m.DateTimeField(auto_now=True)
#     is_published = m.BooleanField(default=True)
#
#     category = m.ForeignKey('Category', on_delete=m.PROTECT, null=True)
#     brand = m.ForeignKey('Brand', on_delete=m.PROTECT, null=True)
#     color = m.ForeignKey('Color', on_delete=m.PROTECT, null=True)
#     slug = m.SlugField(unique=True)
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.title)
#         super(Goods, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return self.title
#
#

#
#
# class Color(m.Model):
#     title = m.CharField(max_length=50)
#     photo = m.ImageField(upload_to="photos/%Y/%m/%d/")
#     slug = m.SlugField(unique=True)
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.title)
#         super(Color, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return self.title
#
#
# class Brand(m.Model):
#     title = m.CharField(max_length=50)
#     photo = m.ImageField(upload_to="photos/%Y/%m/%d/")
#     description = m.TextField()
#     slug = m.SlugField(unique=True)
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.title)
#         super(Brand, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return self.title
#
#
# class Tags(m.Model):
#     title = m.CharField(max_length=50)
#     slug = m.SlugField(unique=True)
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.title)
#         super(Tags, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return self.title


class LookBook(m.Model):
    title = m.CharField(max_length=50)
    small_description = m.CharField(max_length=50)
    description = m.TextField()
    photo = m.ImageField(upload_to="photos/%Y/%m/%d/")
    is_published = m.BooleanField(default=True)

    slug = m.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(LookBook, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_lookbook', kwargs={'pk': self.pk})


class FeaturesAds(m.Model):
    title = m.CharField(max_length=50)
    description = m.TextField(max_length=200)
    photo = m.ImageField(upload_to="photos/%Y/%m/%d/")
    is_published = m.BooleanField(default=False)

    slug = m.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(FeaturesAds, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Subcategories(m.Model):
    title = m.CharField(max_length=50)
    description = m.TextField(blank=True)

    slug = m.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Subcategories, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Status(m.Model):
    title = m.CharField(max_length=35)

    slug = m.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Status, self).save(*args, **kwargs)
