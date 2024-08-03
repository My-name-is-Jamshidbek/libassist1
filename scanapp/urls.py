from django.urls import path
from .views import scan_view, bar_give_book_view

urlpatterns = [
    path('', scan_view, name='scan'),
    path('give/<int:key>/', bar_give_book_view, name='bar_give_book'),
]
