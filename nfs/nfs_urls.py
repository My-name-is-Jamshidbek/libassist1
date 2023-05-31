from django.urls import path
from .views import *

urlpatterns = [
    path('', nfs_accept_code, name='nfs_accept_code')
]