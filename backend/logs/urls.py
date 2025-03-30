from django.urls import path
from . import views

urlpatterns = [
  path ('logs/', views.rocket_log_list, name='rocket_log_list'),]
