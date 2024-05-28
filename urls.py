from django.urls import path
from .views import *
urlpatterns = [
    path('<int:pk>/', Detail.as_view()),
    path('list/', List.as_view()),
    path('', Create.as_view()),
    path('delete/<int:pk>', Delete.as_view())
]