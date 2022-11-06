from django.urls import path
from . import views
urlpatterns = [
    # path("", views.index, name="index"),
    path('', views.UserCreation.as_view()),
    path('check-user-api', views.UserCreationAPI.as_view()),
    path('verify-user/<int:pk>', views.EmailVerification.as_view()),
]
