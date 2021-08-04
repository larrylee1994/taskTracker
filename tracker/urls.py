from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.tracker, name="tracker"),
    path('<int:id>/update/<int:e_id>', views.update, name="update"),
]