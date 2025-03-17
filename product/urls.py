from django.urls import path
from .views import ComputerView,addNewRooms


urlpatterns = [
    path('addnew/',ComputerView.as_view(),name='add new computer'),
    path('addnewrooms/',addNewRooms,name='add new room'),

] 