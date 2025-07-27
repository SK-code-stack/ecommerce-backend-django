
from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('product', views.product, name="product"),
    path('home-homeoutdoor', views.homePage_homeOutdoor, name="home-homeoutdoor"),
    path('home-electronic', views.homePage_electronics, name="home-electronic"),
    path('home-recomended', views.homePage_recomended, name="home-recomended"),
    path('home-deals', views.home_deals, name="home-deals"),

]

