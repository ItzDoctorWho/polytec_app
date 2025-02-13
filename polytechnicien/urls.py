from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('polytechnicien/<int:member_id>/', views.member_view, name='polytechnicien')
]