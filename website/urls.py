from django.urls import path
from . import views
# from website import urls



urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.user_view, name='user'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('user_details/<int:pk>', views.user_details, name='user_details'),
    path('user_delete/<int:pk>', views.user_delete, name='user_delete'),
    path('add_user/', views.add_user, name='add_user'), 
    path('update_user/<int:pk>', views.update_user, name='update_user'),
]