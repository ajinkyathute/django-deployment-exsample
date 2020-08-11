from django.conf.urls import url
from django.urls import path
from fourth_app import views


urlpatterns = [
    path('',views.index,name='index'),
]
