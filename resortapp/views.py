from django.shortcuts import render
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

# Create your views here.

def index(request):
    resortDetails = ResortDetails.objects.all()
    landingPageSlider = LandingPageSlider.objects.all()
    roomsDetail = RoomsDetail.objects.all()
    amenitieHeading = AmenitieHeading.objects.all()
    amenitie = Amenitie.objects.all()
    newsHeading = NewsHeading.objects.all()
    newses = Newses.objects.all()
    return render(request, 'index.html',{
        'resortDetails' : resortDetails,
        'landingPageSlider' : landingPageSlider,
        'roomsDetail' : roomsDetail,
        'amenitieHeading' : amenitieHeading,
        'amenitie' : amenitie,
        'newsHeading' : newsHeading,
        'newses' : newses
    })

def amenities(request):
    resortDetails = ResortDetails.objects.all()
    landingPageSlider = LandingPageSlider.objects.all()
    amenitieHeading = AmenitieHeading.objects.all()
    amenitie = Amenitie.objects.all()
    return render(request, 'amenities.html',{
        'resortDetails' : resortDetails,
        'landingPageSlider' : landingPageSlider,
        'amenitieHeading' : amenitieHeading,
        'amenitie' : amenitie
    })

def gallery(request):
    resortDetails = ResortDetails.objects.all()
    landingPageSlider = LandingPageSlider.objects.all()
    galleryHeading = GalleryHeading.objects.all()
    gallerySliderImage = GallerySliderImage.objects.all()
    galleryMoreImage = GalleryMoreImage.objects.all()
    return render(request, 'gallery.html',{
        'resortDetails' : resortDetails,
        'landingPageSlider' : landingPageSlider,
        'galleryHeading' : galleryHeading,
        'gallerySliderImage' : gallerySliderImage,
        'galleryMoreImage' : galleryMoreImage
    })

def about(request):
    resortDetails = ResortDetails.objects.all()
    landingPageSlider = LandingPageSlider.objects.all()
    about = AboutDetail.objects.all()
    return render(request, 'about.html',{
        'resortDetails' : resortDetails,
        'landingPageSlider' : landingPageSlider,
        'about' : about
    })

def contact(request):
    resortDetails = ResortDetails.objects.all()
    landingPageSlider = LandingPageSlider.objects.all()
    contactHeading = ContactHeading.objects.all()
    return render(request, 'contact.html',{
        'resortDetails' : resortDetails,
        'landingPageSlider' : landingPageSlider,
        'contact' : contactHeading
    })

def story(request):
    resortDetails = ResortDetails.objects.all()
    landingPageSlider = LandingPageSlider.objects.all()
    contactHeading = ContactHeading.objects.all()
    return render(request, 'story.html',{
        'resortDetails' : resortDetails,
        'landingPageSlider' : landingPageSlider,
        'contact' : contactHeading
    })