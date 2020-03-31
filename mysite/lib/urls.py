#lib/urls.py
from django.urls import path
from . import views

urlpatterns = [
                path('lib/',views.index,name='index'),
                path('detail/',views.detail,name='detail') ,
              ]

