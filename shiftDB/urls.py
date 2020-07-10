from django.urls import path
from todolist_app import views

urlpatterns = [
    path('shifts', views.shifts_view, name='shifts_view'),
    path('shifts_add', views.shifts_view, name='shifts_add_view'),
]