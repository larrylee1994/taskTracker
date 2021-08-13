from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('worksheets/', views.worksheets, name="worksheets"),
    path('i18n/', include('django.conf.urls.i18n')),
]
