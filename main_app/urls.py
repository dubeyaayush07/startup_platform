from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('startups/', views.StartupListView.as_view(), name='startups'),
    path('investment_requests/', views.PostListView.as_view(), name='investment_requests'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('startup_stories/', views.startupStories, name='startup-stories'),
    path('startup_stories2/', views.startupStories2, name='startup-stories2'),
    path('mentor_stories/', views.mentorStories, name='mentor-stories'),
    path('mentor_stories2/', views.mentorStories2, name='mentor-stories2'),
]