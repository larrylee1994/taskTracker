from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    # path('register/', views.register),
    path('sign_in/', views.sign_in),
    path('dashboard/', views.dashboard),
    path('user/', views.user_tracker),
    path('tracker/<int:id>', views.user_tracker),
]
