from django.urls import path

from myapp import views


urlpatterns = [

    path('', views.hello),
    path('products/<id>', views.product),
    path('link', views.link, name="job_home"),
    path('job/<int:id>', views.job, name="job_detail"),
    path('greeting', views.greeting, name="hello"),
    path('test/<int:id>', views.test, name="test_job"),
    path('list_job', views.list_job, name="list_job"),
    path('get_job/<int:id>',views.get_job, name="get_job"),
]
