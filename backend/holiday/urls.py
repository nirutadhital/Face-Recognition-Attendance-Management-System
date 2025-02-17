from django.urls import path
from . import views

urlpatterns = [
    path('',views.holiday_list_create_view,name='holiday-list'),
    path('<int:pk>/update/',views.holiday_update_view,name='holiday-edit'),
    path('<int:pk>/delete/',views.holiday_destroy_view,name='holiday-list'),
]