from django.urls import path
from . import views
urlpatterns = [
    path('', views.UserCreation.as_view()),
    path('verify-user/<int:pk>/', views.EmailVerification.as_view()),
]
