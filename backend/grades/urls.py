from django.urls import path
from . import views

urlpatterns = [
    path('',views.grades_list_create_view,name='grades-list'),
    path('<int:pk>/update/',views.grades_update_view,name='grades-edit'),
    path('<int:pk>/delete/',views.grades_destroy_view,name='grades-list'),
]