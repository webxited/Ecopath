# Generated by Django 4.1.6 on 2023-02-15 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenitie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenitie_Heading', models.CharField(max_length=255)),
                ('amenitie_Description', models.CharField(max_length=1000)),
                ('amenitie_Link_Text', models.CharField(max_length=255)),
                ('amenitie_Text_Link', models.CharField(max_length=1000)),
                ('amenitie_SVG_image', models.FileField(upload_to='img/%y')),
            ],
        ),
        migrations.CreateModel(
            name='AmenitieHeading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenities_Heading', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LandingPageSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_1_Heading', models.CharField(max_length=255)),
                ('slider_1_description', models.CharField(max_length=1000)),
                ('slider_1_image', models.ImageField(upload_to='img/%y')),
                ('slider_2_Heading', models.CharField(max_length=255)),
                ('slider_2_description', models.CharField(max_length=1000)),
                ('slider_2_image', models.ImageField(upload_to='img/%y')),
                ('slider_3_Heading', models.CharField(max_length=255)),
                ('slider_3_description', models.CharField(max_length=1000)),
                ('slider_3_image', models.ImageField(upload_to='img/%y')),
                ('slider_4_Heading', models.CharField(max_length=255)),
                ('slider_4_description', models.CharField(max_length=1000)),
                ('slider_4_image', models.ImageField(upload_to='img/%y')),
            ],
        ),
        migrations.CreateModel(
            name='Newses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_Headline', models.CharField(max_length=255)),
                ('news_date', models.DateField()),
                ('news_author', models.CharField(max_length=255)),
                ('news_description', models.CharField(max_length=1000)),
                ('news_Link_Text', models.CharField(max_length=255)),
                ('news_Text_Link', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='NewsHeading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_Heading', models.CharField(max_length=255)),
                ('news_Description', models.CharField(max_length=1000)),
                ('news_Link_Text', models.CharField(max_length=255)),
                ('news_Text_Link', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ResortDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resort_Name', models.CharField(max_length=100)),
                ('resort_Address', models.CharField(max_length=2500)),
                ('resort_Phone', models.CharField(max_length=14)),
                ('resort_Email', models.CharField(max_length=255)),
                ('resort_Facebook', models.CharField(max_length=2500)),
                ('resort_Instagram', models.CharField(max_length=2500)),
                ('resort_Location', models.CharField(max_length=2500)),
                ('resort_Title', models.CharField(max_length=100)),
                ('resort_Favicon', models.ImageField(upload_to='img/%y')),
            ],
        ),
        migrations.CreateModel(
            name='RoomsDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rooms_Heading', models.CharField(max_length=100)),
                ('room_1_heading', models.CharField(max_length=255)),
                ('room_1_description', models.CharField(max_length=1500)),
                ('room_1_link_text', models.CharField(max_length=255)),
                ('room_1_text_link', models.CharField(max_length=1000)),
                ('room_1_image_1', models.ImageField(upload_to='img/%y')),
                ('room_1_image_2', models.ImageField(upload_to='img/%y')),
                ('room_2_heading', models.CharField(max_length=255)),
                ('room_2_description', models.CharField(max_length=1500)),
                ('room_2_link_text', models.CharField(max_length=255)),
                ('room_2_text_link', models.CharField(max_length=1000)),
                ('room_2_image_1', models.ImageField(upload_to='img/%y')),
                ('room_2_image_2', models.ImageField(upload_to='img/%y')),
            ],
        ),
    ]
