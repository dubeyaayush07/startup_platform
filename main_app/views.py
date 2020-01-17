from django.shortcuts import render
from users.models import Profile
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    return render(request, 'main_app/home.html')


class StartupListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Profile
    template_name = 'main_app/startups.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        user_category = self.request.user.profile.category
        return Profile.objects.filter(role='S', category=user_category)


    def test_func(self):
        if self.request.user.profile.role == 'M':
            return True
        return False