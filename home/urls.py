from django.urls import path

from home import views

app_name='home'
urlpatterns = [
    path('', views.index, name='main'),
    path('search', views.search, name='search'),
    path('contacto', views.contacto, name='contacto'),
    path('about', views.about, name='about'),
    path('terms', views.terms, name='terms'),
]
