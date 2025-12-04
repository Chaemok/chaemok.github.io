from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list),        # api/projects/
    path('<int:pk>/', views.project_detail), # api/projects/1/    
]   