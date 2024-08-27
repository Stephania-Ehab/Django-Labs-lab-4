from django.urls import path
from .views import *

urlpatterns = [
    path('', track_list, name="track_list"),
    path('update/<int:id>', track_update, name='track_update'),
    path('delete/<int:id>', track_delete, name='track_delete'),
    path('details/<int:id>', track_details, name='track_details'),
    path('create/', track_create, name='track_create'),
]