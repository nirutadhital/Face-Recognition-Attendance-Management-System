from django.urls import path
from . import views

urlpatterns = [
    path('',views.faculty_list_create_view,name='faculty-list'),
    path('<int:pk>/update/',views.faculty_update_view,name='faculty-edit'),
    path('<int:pk>/delete/',views.faculty_destroy_view,name='faculty-list'),
]