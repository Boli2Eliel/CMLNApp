from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import DetailView
from activite import views

urlpatterns = [

    path('activites/', views.activite, name="activites"),
    path('activite/create', views.CreateActivite.as_view(), name="create_activite"),
    path('activite/update/<int:pk>', views.UpdateActivite.as_view(), name="update_activite"),
    path('activites/<int:pk>', views.DetailActivite.as_view(), name="detail_activite"),
    path('delete_activite/<int:id>', views.delete_activite, name='delete_activite'),

]