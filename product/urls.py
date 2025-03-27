from django.urls import path
from .views import ComputerView,addNewRooms,ComputerDetailView


urlpatterns = [
    path('addnew/',ComputerView.as_view(),name='add new computer'),
    path('compdetails/<int:pk>/', ComputerDetailView.as_view(), name='computer-detail'),
    path('addnewrooms/',addNewRooms,name='add new room'),

] 