from django.urls import path,reverse
from . import views

app_name = 'base_app'

urlpatterns = [
    path('',views.index,name='home'),
    path('reset/', views.reset,name='reset'),
]