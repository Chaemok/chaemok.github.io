from django.urls import path
from . import views    

urlpatterns = [
    path('skills/', views.skill_list),
    path('skills/<int:pk>/', views.skill_detail),
    path('timelines/', views.timeline_list),
    path('posts/', views.post_list),
    path('posts/<int:pk>/', views.post_detail),
    path('guestbook/', views.guestbook_list),
    path('contact/', views.contact_create),
]