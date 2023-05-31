from django.urls import path
from .views import main, return_book

urlpatterns = [
    path('<int:id>/', main, name='main'),
    path('<int:id>/remove', return_book, name='remove'),
]
