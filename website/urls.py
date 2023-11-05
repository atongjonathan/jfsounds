from . import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('audio', views.audio, name='audio'),
    path('special', views.special, name='special'),
    path('lighting', views.lighting, name='lighting'),
    path('backline', views.backline, name='backline'),
    path('staging', views.staging, name='staging'),
    path('featuredwork', views.work, name='work'),
    path('careers', views.careers, name='careers'),
    path('avequipment', views.av, name='av'),
    path('contact', views.contact, name='contact')
]