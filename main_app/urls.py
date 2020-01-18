from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('startups/', views.StartupListView.as_view(), name='startups'),
]