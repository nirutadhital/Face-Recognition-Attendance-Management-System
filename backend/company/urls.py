from django.urls import path
from . import views

urlpatterns = [
    path('',views.company_list_create_view,name='company-list'),
    path('<int:pk>/update/',views.company_update_view,name='company-edit'),
    path('<int:pk>/delete/',views.company_destroy_view,name='company-list'),
]