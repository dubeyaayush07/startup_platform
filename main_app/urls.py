from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('startups/', views.StartupListView.as_view(), name='startups'),
]