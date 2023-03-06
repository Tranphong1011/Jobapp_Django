from register import views
from django.urls import path

urlpatterns = [
    path('register/', views.register, name='register'),
    path('thank/', views.thank_you, name='thank_you'),
]
