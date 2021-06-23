from django.contrib import admin
from django.urls import path
from operation import views
urlpatterns = [
   path("", views.index, name='index'),
   path("delete/<int:id>",views.deletedata,name="deletedata"),
   path("<int:id>/",views.updatedata,name="updatedata")
]