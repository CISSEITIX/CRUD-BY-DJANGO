from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . views import * 


urlpatterns = [
      path('', index, name='index'),
      path('add_item', add_item, name='add_item'),
      path('delete_item/<int:myid>/', delete_item, name='delete_item'),
      path('edit_item/<int:Id>/', edit_item, name='edit_item'),
      path('update_item/<int:Id>/',update_item, name='update_item'),
  ]