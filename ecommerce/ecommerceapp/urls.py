from django.urls import path
from ecommerceapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('contacts',views.contact,name="contact"),
    path('about',views.about,name="about"),
]
