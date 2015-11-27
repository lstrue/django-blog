'''
Created on Nov 26, 2015
 
@author: davidli
'''
 
from django.conf.urls import url
from . import views
 
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
