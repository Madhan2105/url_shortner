from django.urls import path
from . import views


urlpatterns = [
    path('', views.url_shortener, name='url_shortener'),
    path('api/', views.url_shortener, name='url_shortener'),
    path('api/<str:optional_slug>', views.url_shortener, name='url_shortener_get'),
    path('goto/<slug:slug>/', views.redirect_site),
]