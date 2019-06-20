from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from exampleapi import views

urlpatterns = [
    path('courses/', views.CourseList.as_view()),
    path('courses/<int:pk>/', views.CourseDetail.as_view()),
]
