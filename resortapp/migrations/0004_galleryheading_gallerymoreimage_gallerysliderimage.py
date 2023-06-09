# Generated by Django 4.1.6 on 2023-02-15 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resortapp', '0003_newses'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryHeading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_Heading', models.CharField(max_length=255)),
                ('gallery_Slider_Heading', models.CharField(max_length=255)),
                ('gallery_More_Heading', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryMoreImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('more_description', models.CharField(max_length=255)),
                ('more_LargeImage_1', models.ImageField(upload_to='img/%y')),
                ('more_LargeImage_2', models.ImageField(upload_to='img/%y')),
                ('more_SmallImage_1', models.ImageField(upload_to='img/%y')),
                ('more_SmallImage_2', models.ImageField(upload_to='img/%y')),
                ('more_SmallImage_3', models.ImageField(upload_to='img/%y')),
                ('more_LargeImage_3', models.ImageField(upload_to='img/%y')),
                ('more_LargeImage_4', models.ImageField(upload_to='img/%y')),
            ],
        ),
        migrations.CreateModel(
            name='GallerySliderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_description', models.CharField(max_length=255)),
                ('slider_image', models.ImageField(upload_to='img/%y')),
            ],
        ),
    ]
