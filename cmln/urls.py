from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import DetailView

from .models.model_aerd import Aerd
from .models.model_membre import Membre
from .views import view_home, view_membre, view_aerd

urlpatterns = [
    path('', view_home.index, name="home"),
    path('membre/', view_membre.membre_list, name="membres"),
    path('membre/create', view_membre.CreateMembre.as_view(), name="create_membre"),
    path('membre/update/<int:pk>', view_membre.UpdateMembre.as_view(), name="update_membre"),
    path('membres/<int:pk>', login_required(DetailView.as_view(model=Membre, template_name="cmln/membre/membre_detail.html")), name="detail_membre"),

    path('aerd/', view_aerd.aerd_list, name="aerds"),
    path('aerd/create', view_aerd.CreateAerd.as_view(), name="create_aerd"),
    path('aerd/update/<int:pk>', view_aerd.UpdateAerd.as_view(), name="update_aerd"),
    path('aerds/<int:pk>', login_required(DetailView.as_view(model=Aerd, template_name="cmln/aerd/aerd_detail.html")), name="detail_aerd")

]