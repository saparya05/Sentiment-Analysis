from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('SentimentAnalysis', views.SentimentAnalysis, name='SentimentAnalysis')
]