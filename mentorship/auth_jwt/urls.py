from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name="registration"),
    path('sign-in/', views.sign_in, name="sign_in"),
    path('', views.redirect_index, name="auth"),
]
