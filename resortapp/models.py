from django.db import models

# Create your models here.

class ResortDetails(models.Model):
    resort_Name = models.CharField(max_length=100)
    resort_Address = models.CharField(max_length=2500)
    resort_Phone = models.CharField(max_length=14)
    resort_Email = models.CharField(max_length=255)
    resort_Facebook = models.CharField(max_length=2500)
    resort_Instagram = models.CharField(max_length=2500)
    resort_Location = models.CharField(max_length=2500)
    resort_Title = models.CharField(max_length=100)
    resort_Favicon = models.ImageField(upload_to="img/%y")

class LandingPageSlider(models.Model):
    slider_1_Heading = models.CharField(max_length=255)
    slider_1_description = models.CharField(max_length=1000)
    slider_1_image = models.ImageField(upload_to="img/%y")
    slider_2_Heading = models.CharField(max_length=255)
    slider_2_description = models.CharField(max_length=1000)
    slider_2_image = models.ImageField(upload_to="img/%y")
    slider_3_Heading = models.CharField(max_length=255)
    slider_3_description = models.CharField(max_length=1000)
    slider_3_image = models.ImageField(upload_to="img/%y")
    slider_4_Heading = models.CharField(max_length=255)
    slider_4_description = models.CharField(max_length=1000)
    slider_4_image = models.ImageField(upload_to="img/%y")

class RoomsDetail(models.Model):
    rooms_Heading = models.CharField(max_length=100)
    room_1_heading = models.CharField(max_length=255)
    room_1_description = models.CharField(max_length=1500)
    room_1_link_text = models.CharField(max_length=255)
    room_1_text_link = models.CharField(max_length=1000)
    room_1_image_1 = models.ImageField(upload_to="img/%y")
    room_1_image_2 = models.ImageField(upload_to="img/%y")
    room_2_heading = models.CharField(max_length=255)
    room_2_description = models.CharField(max_length=1500)
    room_2_link_text = models.CharField(max_length=255)
    room_2_text_link = models.CharField(max_length=1000)
    room_2_image_1 = models.ImageField(upload_to="img/%y")
    room_2_image_2 = models.ImageField(upload_to="img/%y")

class AmenitieHeading(models.Model):
    amenities_Heading = models.CharField(max_length=255)

class Amenitie(models.Model):
    amenitie_Heading = models.CharField(max_length=255)
    amenitie_Description = models.CharField(max_length=1000)
    amenitie_Link_Text = models.CharField(max_length=255)
    amenitie_Text_Link = models.CharField(max_length=1000)
    amenitie_SVG_image = models.FileField(upload_to="img/%y")

class NewsHeading(models.Model):
    news_Heading = models.CharField(max_length=255)
    news_Description = models.CharField(max_length=1000)
    news_Link_Text = models.CharField(max_length=255)
    news_Text_Link = models.CharField(max_length=1000)

class Newses(models.Model):
    news_Headline = models.CharField(max_length=255)
    news_date = models.DateField()
    news_author = models.CharField(max_length=255)
    news_description = models.CharField(max_length=1000)
    news_Link_Text = models.CharField(max_length=255)
    news_Text_Link = models.CharField(max_length=1000)
    news_image = models.ImageField(upload_to="img/%y")

class GalleryHeading(models.Model):
    gallery_Heading = models.CharField(max_length=255)
    gallery_Slider_Heading = models.CharField(max_length=255)
    gallery_More_Heading = models.CharField(max_length=255)

class GallerySliderImage(models.Model):
    slider_description = models.CharField(max_length=255)
    slider_image = models.ImageField(upload_to="img/%y")

class GalleryMoreImage(models.Model):
    more_description = models.CharField(max_length=255)
    more_LargeImage_1 = models.ImageField(upload_to="img/%y")
    more_LargeImage_2 = models.ImageField(upload_to="img/%y")
    more_SmallImage_1 = models.ImageField(upload_to="img/%y")
    more_SmallImage_2 = models.ImageField(upload_to="img/%y")
    more_SmallImage_3 = models.ImageField(upload_to="img/%y")
    more_LargeImage_3 = models.ImageField(upload_to="img/%y")
    more_LargeImage_4 = models.ImageField(upload_to="img/%y")

class AboutDetail(models.Model):
    about_Heading = models.CharField(max_length=255)
    about_Description = models.CharField(max_length=1000)
    about_Management_Heading = models.CharField(max_length=255)
    about_Management_SubHeading = models.CharField(max_length=255)
    about_Management_Description_P1 = models.CharField(max_length=1000)
    about_Management_Description_P2 = models.CharField(max_length=1000)
    about_Management_Description_P3 = models.CharField(max_length=1000)
    about_Management_Image = models.ImageField(upload_to="img/%y")
    about_Video_Heading = models.CharField(max_length=255)
    about_Video_Description_P1 = models.CharField(max_length=1000)
    about_Video_Description_P2 = models.CharField(max_length=1000)
    about_Video = models.FileField(upload_to="img/%y")

class ContactHeading(models.Model):
    contact_Heading = models.CharField(max_length=255)
    contact_Map_Heading = models.CharField(max_length=255)