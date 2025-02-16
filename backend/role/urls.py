from django.urls import path
from . import views

urlpatterns = [
    path('',views.role_list_create_view, name='role-list'),
    path('<int:pk>/update/',views.role_update_view, name='role-edit'),
    path('<int:pk>/delete/',views.role_destroy_view, name='role-delete'),
]