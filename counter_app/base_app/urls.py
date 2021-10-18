from django.urls import path,reverse,include
from . import views

app_name = 'base_app'

urlpatterns = [
    path('',views.index,name='home'),
    path('reset/', views.reset,name='reset'),
    path('api/',include('api.urls')),
]