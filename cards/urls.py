from django.urls import path
from . import views

app_name = 'cards'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
]
"""    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='detail'),"""
