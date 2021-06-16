from django.urls import path, include
#from . import views
from pybo import views

urlpatterns = [
    path('pybo/', views.index),
    path('pybo/<int:question_id>/', views.detail),
]
