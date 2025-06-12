from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('submit/', views.submit_form, name='submit_form'),
]
# This file defines the URL patterns for the contactme app.
# It maps the root URL to the index view and the submit URL to the submit_form view.