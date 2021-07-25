from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('dashboard/', views.dashboard),
    path('user/', views.user_tracker),
    path('tracker/<int:id>', views.user_tracker),
]
