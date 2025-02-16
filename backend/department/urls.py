from django.urls import path
from . import views

urlpatterns = [
    path('',views.department_list_create_view, name='department-list'),
    path('<int:pk>/update/',views.department_update_view, name='department-edit'),
    path('<int:pk>/delete/',views.department_destroy_view, name='department-delete'),
]