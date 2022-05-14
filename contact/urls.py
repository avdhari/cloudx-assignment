from django.urls import path
from contact import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('success/', views.success_view, name='success-page'),
]
