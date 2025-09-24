from django.urls import path
from news import views


urlpatterns = [
    path('retrieve/', views.get_news),
    path('create/<int:id>/', views.create_news),
    path('update/<int:id>/', views.update_news),
    path('delete/<int:id>/', views.delete_news),
    path('likes/<int:id>/', views.like_news)
]