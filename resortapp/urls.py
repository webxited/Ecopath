from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = "resortapp"),
    path('amenities/',views.amenities, name = "amenities"),
    path('gallery/', views.gallery, name = "gallery"),
    path('about/', views.about, name = "about"),
    path('contact/', views.contact, name = "contact"),
    path('story/', views.story, name = "story")
]

