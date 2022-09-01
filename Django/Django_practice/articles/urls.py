from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('show/<name>/', views.show, name='show'),  # <>변수 같은거임, <str:name> <int:key> <- 라우터이고 str이 default값이고 생략가능
]