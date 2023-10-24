from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import DetailView

from stats.views import dons_list

urlpatterns = [

    path('dons/',dons_list, name="dons_list"),

]