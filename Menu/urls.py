
from . import views

from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [

path('Granola', views.Granola,name='Granola'),

path('ProteinBites', views.ProteinBites,name='ProteinBites'),

path('Bowls', views.Bowls,name='Bowls')

]
urlpatterns += staticfiles_urlpatterns()