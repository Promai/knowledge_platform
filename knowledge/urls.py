from django.urls import path
from . import views

urlpatterns = [
    path('', views.knowledge_list, name='knowledge_list'),
    path('<int:pk>/', views.knowledge_detail, name='knowledge_detail'),
]