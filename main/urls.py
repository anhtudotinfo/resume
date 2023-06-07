from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    # post views
    path('', views.home, name='home'),
    path('resume', views.resume, name='resume'),
    path('projects', views.projects, name='projects'),
    path('inspirations', views.inspirations, name='inspirations'),
    path('contact', views.contact, name='contact'),
]

