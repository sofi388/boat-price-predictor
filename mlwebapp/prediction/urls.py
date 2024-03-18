from django.urls import path
from . import views

app_name = 'prediction'

urlpatterns = [
    # ('', views.predict_sentiment, name='predict_sentiment'),
    path('', views.index, name='index'),
    path('predict/', views.predict, name='predict'),
    path('info/', views.info, name='info'),
    path('result/', views.result, name='result'),

]

handler404 = 'prediction.views.handler404'
