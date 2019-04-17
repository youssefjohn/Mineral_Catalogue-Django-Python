from . import views
from django.urls import path, include


urlpatterns = [

    path('main_page', views.index, name="index" ),
    path('<int:pk>/', views.details, name="details"),

]