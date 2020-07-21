from django.contrib import admin
from django.urls import path
from parlor import views
urlpatterns = [
    path('', views.index,name='parlor'),
    path('about', views.about,name='about'),
    path('services', views.services,name='services'),
    path('contact', views.contact,name='contact'),
    path('chocolate', views.chocolate,name='chocolate'),
    path('butterscotch', views.butterscotch,name='butterscotch'),
    path('familypack', views.familypack,name='familypack'),
    
]
