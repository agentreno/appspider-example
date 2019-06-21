from django.urls import path
from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from exampleapi import views

schema_view = get_schema_view(
   openapi.Info(
      title="AppSpider Example API",
      default_version='v1',
      description="An API to test AppSpider DAST"
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url('^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('courses/', views.CourseList.as_view()),
    path('courses/<int:pk>/', views.CourseDetail.as_view()),
]
