from uploadapp import views
from django.urls import path


urlpatterns = [
    path('images', views.uploadapp, name ='addimage'),
    # path('thank/', views.thank_you, name='thank_you'),
    path('files', views.uploadfile, name ='addfile'),
]
