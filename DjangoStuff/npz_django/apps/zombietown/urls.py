from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('bob',views.bob),
    path('bob/bankaccount', views.money)
]