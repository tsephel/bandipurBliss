from django.urls import path
from .views import home_view, success_view, failure_view

urlpatterns = [
    path('', home_view, name='home'),
    path('success/', success_view, name='success'),
    path('failure/', failure_view, name='failure'),
  
]
