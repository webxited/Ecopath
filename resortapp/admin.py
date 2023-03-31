from django.contrib import admin
from .models import ResortDetails
from .models import LandingPageSlider
from .models import RoomsDetail
from .models import AmenitieHeading
from .models import Amenitie
from .models import NewsHeading
from .models import Newses
from .models import GalleryHeading
from .models import GallerySliderImage
from .models import GalleryMoreImage
from .models import AboutDetail
from .models import ContactHeading

# Register your models here.

class ResortDetailsAdmin(admin.ModelAdmin):
    list_display = ('resort_Name','resort_Address','resort_Phone','resort_Email','resort_Facebook','resort_Instagram','resort_Location',
                    'resort_Title','resort_Favicon',)
    
class LandingPageSliderAdmin(admin.ModelAdmin):
    list_display = ('slider_1_Heading','slider_1_description','slider_1_image',
                    'slider_2_Heading','slider_2_description','slider_2_image',
                    'slider_3_Heading','slider_3_description','slider_3_image',
                    'slider_4_Heading','slider_4_description','slider_4_image',)
    
class RoomsDetailAdmin(admin.ModelAdmin):
    list_display = ('rooms_Heading','room_1_heading','room_1_description','room_1_link_text','room_1_text_link','room_1_image_1','room_1_image_2',
                    'room_2_heading','room_2_description','room_2_link_text','room_2_text_link','room_2_image_1','room_2_image_2',)
    
class AmenitieHeadingAdmin(admin.ModelAdmin):
    list_display = ('amenities_Heading',)

class AmenitieAdmin(admin.ModelAdmin):
    list_display = ('amenitie_Heading','amenitie_Description','amenitie_Link_Text','amenitie_Text_Link','amenitie_SVG_image',)

class NewsHeadingAdmin(admin.ModelAdmin):
    list_display = ('news_Heading','news_Description','news_Link_Text','news_Text_Link',)

class NewsesAdmin(admin.ModelAdmin):
    list_display = ('news_Headline','news_date','news_author','news_description','news_Link_Text','news_Text_Link','news_image',)

class GalleryHeadingAdmin(admin.ModelAdmin):
    list_display = ('gallery_Heading','gallery_Slider_Heading','gallery_More_Heading',)

class GallerySliderImageAdmin(admin.ModelAdmin):
    list_display = ('slider_description','slider_image',)

class GalleryMoreImageAdmin(admin.ModelAdmin):
    list_display = ('more_description','more_LargeImage_1','more_LargeImage_2','more_SmallImage_1','more_SmallImage_2',
                    'more_SmallImage_3','more_LargeImage_3','more_LargeImage_4',)

class AboutDetailAdmin(admin.ModelAdmin):
    list_display = ('about_Heading','about_Description','about_Management_Heading','about_Management_SubHeading','about_Management_Description_P1',
                    'about_Management_Description_P2','about_Management_Description_P3','about_Management_Image','about_Video_Heading',
                    'about_Video_Description_P1','about_Video_Description_P2','about_Video',)
    
class ContactHeadingAdmin(admin.ModelAdmin):
    list_display = ('contact_Heading','contact_Map_Heading',)

admin.site.register(ResortDetails,ResortDetailsAdmin)
admin.site.register(LandingPageSlider,LandingPageSliderAdmin)
admin.site.register(RoomsDetail,RoomsDetailAdmin)
admin.site.register(AmenitieHeading,AmenitieHeadingAdmin)
admin.site.register(Amenitie,AmenitieAdmin)
admin.site.register(NewsHeading,NewsHeadingAdmin)
admin.site.register(Newses,NewsesAdmin)
admin.site.register(GalleryHeading,GalleryHeadingAdmin)
admin.site.register(GallerySliderImage,GallerySliderImageAdmin)
admin.site.register(GalleryMoreImage,GalleryMoreImageAdmin)
admin.site.register(AboutDetail,AboutDetailAdmin)
admin.site.register(ContactHeading,ContactHeadingAdmin)