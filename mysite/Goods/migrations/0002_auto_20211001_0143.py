# Generated by Django 3.2.7 on 2021-09-30 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LookBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('small_description', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='goods',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='category',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='color',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.DeleteModel(
            name='Goods',
        ),
    ]