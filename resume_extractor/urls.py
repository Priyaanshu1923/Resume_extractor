from django.contrib import admin
from django.urls import path
from resumeapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload_resume, name='upload_resume'),
    path('', views.home, name='home'),  # Add this line
]
