from accounts import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('manage_stack/', views.manage_stack, name='manage_stack'),
    path('manage_stack_left/', views.manage_stack_left, name='manage_stack_left'),
    path('manage_stack_new_set_modal/', views.manage_stack_new_set_modal, name='manage_stack_new_set_modal'),
]
