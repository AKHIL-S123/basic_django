from django.urls import path
from . import views

urlpatterns = [
    path('', views.person_list, name='person_list'),
    path('person/create/', views.person_create, name='person_create'),
    path('person/<int:pk>/update/', views.person_update, name='person_update'),
    path('person/<int:pk>/delete/', views.person_delete, name='person_delete'),
]
