from unicodedata import name
from django.urls import path
from library.superadmin import *

urlpatterns = [
    path('', superadmin, name='superadmin'),
    path('settings/', addemployee, name='superadmin_settings'),
    path('messages/', superadmin_messages, name='superadmin_messages'),
    path('all_book', all_book, name='all_book_admin'),
    path('reading_book', bookers, name='bookers_admin'),
    path('sendmessagese', employeesend, name='employeesend'),
    path('studentsend', studentsend, name='studentsend'),
    path('addemployee', addemployee, name='addemployee'),
    path('delemployee', delemployee, name='delemployee'),
    path('delemployee/<id>', del_e, name='del_e'),
    path('employee', employee, name='employee'),
    path('student_select', talaba_tanla_admin, name='student_select'),
    path('student_select/<id>', talaba_admin, name='student_admin'),
    path('contact', contact_a, name='contact_a')
]