# blooddonor/urls.py

from django.urls import path
from .views import (
    register_user, login_user, logout_user, donor_list, donor_detail,
    create_donor, edit_donor, delete_donor
)

urlpatterns = [
    path('', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('donors/', donor_list, name='donor_list'),
    path('donors/<int:donor_id>/', donor_detail, name='donor_detail'),
    path('donors/create/', create_donor, name='create_donor'),
    path('donors/<int:donor_id>/edit/', edit_donor, name='edit_donor'),
    path('donors/<int:donor_id>/delete/', delete_donor, name='delete_donor'),
]



