from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import DetailView

from .models.model_aerd import Aerd
from .models.model_membre import Membre
from .views import view_home, view_membre, view_aerd, view_activite, view_finances
from .views.view_membre import MembreAutocomplete


urlpatterns = [
    path('', view_home.index, name="home"),

    #DASHBOARD
    path('dashboard1/', view_home.dashboard1, name="dashboard1"),

    #DASHBOARD
    path('dons/', view_finances.dons_list, name="dons"),


    #MEMBRE
    path('membre/', view_membre.membre_list, name="membres"),
    path('membre/create', view_membre.CreateMembre.as_view(), name="create_membre"),
    #path('membre/create', view_membre.createMembre, name="create_membre"),
    path('membre/update/<int:pk>', view_membre.UpdateMembre.as_view(), name="update_membre"),
    path('membres/<int:pk>', login_required(DetailView.as_view(model=Membre, template_name="cmln/membre/membre_detail.html")), name="detail_membre"),
    path('membres/autocomplete/', login_required(MembreAutocomplete.as_view()), name="membre_autocomplete"),
    path('delete_membre/<int:id>', view_membre.delete_membre, name='delete_membre'),

    #AERD
    path('aerd/', view_aerd.aerd_list, name="aerds"),
    #path('aerd/create', view_aerd.aerd_create, name="create_aerd"),
    path('aerd/create', view_aerd.CreateAerd.as_view(), name="create_aerd"),
    path('aerd/update/<int:pk>', view_aerd.UpdateAerd.as_view(), name="update_aerd"),
    #path('aerds/<int:pk>', login_required(DetailView.as_view(model=Aerd, template_name="cmlnGestion/aerd/aerd_detail.html")), name="detail_aerd"),
    path('aerds/<int:pk>',view_aerd.DetailAerd.as_view(), name="detail_aerd"),
    path('delete_aerd/<int:id>', view_aerd.delete_aerd, name='delete_aerd'),

    path('activites/', view_activite.activite, name="activites"),
    path('activite/create', view_activite.CreateActivite.as_view(), name="create_activite"),
    path('activite/update/<int:pk>', view_activite.UpdateActivite.as_view(), name="update_activite"),
    path('activites/<int:pk>',view_activite.DetailActivite.as_view(), name="detail_activite"),
    path('delete_activite/<int:id>', view_activite.delete_activite, name='delete_activite'),

]