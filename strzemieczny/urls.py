from django.urls import path, include
from .views import (
    myProjectsView,
)

urlpatterns = [
    path('api/', myProjectsView.as_view()),
]
