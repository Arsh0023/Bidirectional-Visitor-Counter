from django.urls import path
from . import views

urlpatterns = [
    path('getvisitorin/<str:passphrase>/', views.getvisitorin, name='getvisitorin'),
    path('setvisitorin/<str:passphrase>/', views.setvisitorin, name='setvisitorin'),
    path('getvisitorout/<str:passphrase>/', views.getvisitorout, name='getvisitorout'),
    path('setvisitorout/<str:passphrase>/', views.setvisitorout, name='setvisitorout'),
]