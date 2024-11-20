from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('pregunta_1/', views.pregunta_1, name='pregunta_1'),
    path('pregunta_2/', views.pregunta_2, name='pregunta_2'),
    path('pregunta_3/', views.pregunta_3, name='pregunta_3'),
    path('pregunta_4/', views.pregunta_4, name='pregunta_4'),
    path('pregunta_5/', views.pregunta_5, name='pregunta_5'),
    path('fin/', views.fin, name='fin'),
    

]
