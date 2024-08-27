from django.urls import path
from .views import *

urlpatterns = [
    path('', trainee_list, name='trainee_list'),
    path('update/<int:id>', trainee_update, name='trainee_update'),
    path('delete/<int:id>', trainee_delete, name='trainee_delete'),
    path('details/<int:id>', trainee_details, name='trainee_details'),
    path('create/', trainee_create, name='trainee_create'),
    path('createform/', trainee_create_form, name='trainee_create_form'),
    path('createformmodel/',trainee_create_formmodel,name='trainee_create_formmodel')
]