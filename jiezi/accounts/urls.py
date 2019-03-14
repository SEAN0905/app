from accounts import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('manage_stack/', views.manage_stack, name='manage_stack'),
    path('manage_stack_left/', views.manage_stack, {'is_left': True}, name='manage_stack_left'),
    path('manage_stack_right/', views.manage_stack, {'is_right': 0}, name='manage_stack_right'),
    path('manage_stack_new_set/', views.manage_stack, {'is_new_set': True}, name='manage_stack_new_set'),
]