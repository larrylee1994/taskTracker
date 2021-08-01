from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('worksheets/', views.worksheets, name="worksheets"),
]
