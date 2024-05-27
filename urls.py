from django.urls import path
from .views import *
urlpatterns = [
    path('<int:pk>/', Detail.as_view()),
    path('', List.as_view()),
    path('create', Create.as_view()),
    path('delete/<int:pk>', Delete.as_view())
]