from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_signup_view, name='user-signup'),
    # path('<int:pk>/update/',views.user_update_view, name='user-edit'),
    # path('<int:pk>/delete',views.user_destroy_view, name='user-delete'),
]
