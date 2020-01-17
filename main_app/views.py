from django.shortcuts import render
from users.models import Profile
from django.views.generic import ListView


def home(request):
    return render(request, 'main_app/home.html')


class StartupListView(ListView):
    model = Profile
    template_name = 'main_app/startups.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.filter(role='S')