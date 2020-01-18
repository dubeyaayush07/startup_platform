"""startup_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from chat import views as chat_views
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf.urls import url




urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('dashboard/', user_views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('main_app.urls')),
    path('arooms/', chat_views.all_rooms, name="all_rooms"),
    url(r'rooms/(?P<slug>[-\w]+)/$', chat_views.room_detail, name="room_detail"),
    url(r'token$', chat_views.token, name="token"),
    path('add_room/<str:username>', chat_views.add_room, name='add_room'),
]
