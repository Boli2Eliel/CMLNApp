from django.urls import path
from . import views

app_name = "avancee"

urlpatterns = [

    # Extensions
    path('extensions/', views.list_extension, name="extensions"),
    path('extension/create', views.CreateExtension.as_view(), name="create_extension"),
    path('extension/update/<int:pk>', views.UpdateExtension.as_view(), name="update_extension"),
    path('extension/<int:pk>', views.DetailExtension.as_view(), name="detail_extension"),
    path('delete_extension/<int:id>', views.delete_extension, name='delete_extension'),

    # Ministeres
    path('ministeres/', views.list_ministeres, name="ministeres"),
    path('ministere/create', views.CreateMinistere.as_view(), name="create_ministere"),
    path('ministere/update/<int:pk>', views.UpdateMinistere.as_view(), name="update_ministere"),
    path('ministere/<int:pk>', views.DetailMinistere.as_view(), name="detail_ministere"),
    path('delete_ministere/<int:id>', views.delete_ministere, name='delete_ministere'),

]
