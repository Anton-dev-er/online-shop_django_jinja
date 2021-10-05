from django.db import models as m
from slugify import slugify
from django.urls import reverse


class Goods(m.Model):
    title = m.CharField(max_length=50)
    small_description = m.CharField(max_length=50)
    description = m.TextField()
    price = m.IntegerField()
    photo = m.ImageField(upload_to="photos/%Y/%m/%d/")

    is_discount = m.BooleanField(default=False)
    discount_price = m.IntegerField(blank=True)
    description_discount_price = m.TextField(blank=True)

    created_dt = m.DateTimeField(auto_now_add=True)
    updated_dt = m.DateTimeField(auto_now=True)
    is_published = m.BooleanField(default=True)

    category = m.ForeignKey('SubCategories', on_delete=m.PROTECT, null=True)

    size = m.CharField(max_length=50, default="Потом допилю(розмір)")
    brand = m.CharField(max_length=50, default="Потом допилю(бренд)")
    color = m.CharField(max_length=50, default="Потом допилю(цвет)")
    material = m.CharField(max_length=50, default="Потом допилю(Материал)")

    slug = m.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Goods, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class LookBook(m.Model):
    title = m.CharField(max_length=50)
    small_description = m.CharField(max_length=50)
    description = m.TextField()
    photo = m.ImageField(upload_to="photos/%Y/%m/%d/")
    is_published = m.BooleanField(default=True)

    slug = m.SlugField(unique=True, blank=True)

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

    slug = m.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(FeaturesAds, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class BroadCategories(m.Model):
    title = m.CharField(max_length=200)

    slug = m.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BroadCategories, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Categories(m.Model):
    title = m.CharField(max_length=200)

    created_dt = m.DateTimeField(auto_now_add=True)
    updated_dt = m.DateTimeField(auto_now=True)

    slug = m.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        cleaned_title = self.title.split(":")[0]
        self.title = f"{cleaned_title}:{self.broad_category.title}"
        self.slug = slugify(self.title)
        super(Categories, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('---', kwargs={'slug': self.slug})


class SubCategories(m.Model):
    title = m.CharField(max_length=200)
    category = m.ForeignKey('Categories', on_delete=m.PROTECT)
    broad_category = m.ForeignKey('BroadCategories', on_delete=m.PROTECT)

    created_dt = m.DateTimeField(auto_now_add=True)
    updated_dt = m.DateTimeField(auto_now=True)

    slug = m.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        cleaned_title = self.title.split(":")[0]
        self.title = f"{cleaned_title}:{self.category.title}:{self.broad_category.title}"
        self.slug = slugify(self.title)
        super(SubCategories, self).save(*args, **kwargs)

    def __str__(self):
        return self.title.split(":")[0]

    def get_absolute_url(self):
        return reverse('---', kwargs={'slug': self.slug})


class Status(m.Model):
    title = m.CharField(max_length=35)

    slug = m.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Status, self).save(*args, **kwargs)
