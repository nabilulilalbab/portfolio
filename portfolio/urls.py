from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.index, name='index'),
    path('project_list/', views.project_list, name='project_list'),
    path('project_detail/<int:project_id>/', views.project_detail, name='project_detail'),
    path('contact/', views.contact_view, name='contact'),
    path('profile/', views.profile_view, name='profile'),
]