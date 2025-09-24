from django.urls import path
from users import views



urlpatterns = [
    path('register/', views.Register),
    path('Login/', views.Login)
]