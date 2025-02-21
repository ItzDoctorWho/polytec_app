from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('members/', views.members_list, name='members_list'),
    path("members/update/<int:member_id>/", views.update_member, name="update_member"),
    path("members/delete/<int:member_id>/", views.delete_member, name="delete_member"),
    path('polytechnicien/<int:member_id>/', views.member_view, name='polytechnicien')
]