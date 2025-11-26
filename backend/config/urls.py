"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from skills import views  # views 파일 가져오기

urlpatterns = [
    path('admin/', admin.site.urls),
    # 이 주소로 들어오면 skill_list 함수 실행!
    path('api/skills/', views.skill_list),
    path('api/skills/<int:pk>/', views.skill_detail),
    path('api/projects/', views.project_list),
    path('api/projects/<int:pk>/', views.project_detail),
    path('api/timelines/', views.timeline_list),
    path('api/posts/', views.post_list),
    path('api/posts/<int:pk>/', views.post_detail),
    path('api/guestbook/', views.guestbook_list),
]
