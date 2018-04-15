from django.conf.urls import url, include
from . import views


urlpatterns = [ 
                url(r'^escuela/$', views.viewEscuela, name='viewEscuela'),
                url(r'^escuela/nueva$', views.newEscuela, name='newEscuela'),
                
                url(r'^egresado/$', views.viewEgresado, name='viewEgresado'),  
                url(r'^egresado/nueva$', views.newEgresado, name='newEgresado'), 

                url(r'^insertarPost/$', views.insertarPost, name='insertarPost'), 
                              
            ]