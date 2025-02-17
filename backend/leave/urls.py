from django.urls import path
from . import views

urlpatterns = [
    path('',views.leave_list_create_view,name='leave-list'),
    path('<int:pk>/update/',views.leave_update_view,name='leave-edit'),
    path('<int:pk>/delete/',views.leave_destroy_view,name='leave-list'),
]