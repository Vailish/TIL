from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    # path('new/', views.new, name='new'),   # create와 합쳐짐
    path('create/', views.create, name='create'),  # GET / POST
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    # path('<int:pk>/edit/', views.edit, name='edit'),  # update와 합쳐짐
    path('<int:pk>/update/', views.update, name='update'),  # GET / POST
]
