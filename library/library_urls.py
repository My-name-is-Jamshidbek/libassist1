from django.urls import path
from .settings import *
from .services import *
from .staff import staff, staff_sozlamalar, staff_xizmatlar
from .students import *
from .menu_view import *
from .staff import *


urlpatterns = [
### Staff
	path('', staff, name='staff'),
	path('settings/', staff_sozlamalar, name='staff_settings'),
	path('xizmtalar/', staff_xizmatlar, name='staff_xizmtalar'),
### Settings
	path('groups/', groups, name='groups'),
	path('del_group/<id>', del_g, name='del_g'),
	path('add_student/', add_student, name='add_student'),
	path('del_student', del_student, name='del_student'),
	path('del_student/<id>', del_s, name='del_s'),
	path('add_book', add_book, name='add_book'),
	path('del_book', del_book, name='del_book'),
	path('del_book/<id>', del_book_id, name='del_book_id'),
#### Servise
	path('book_in', book_in, name='book_in'),
	path('book_in/<id>', bookIn, name='bookIn'),
	path('return_book', return_book, name='return_book'),
	path('return_book/<id>', return_user, name='return_user'),
	path('notime', notime, name='notime'),
	path('allreading', allreading, name='allreading'),
	path('check', checkbook, name='check'),
	path('check/<id>', checkdate, name='checkdate'),
	path('check/del/<id>', delcheck, name='delcheck'),
### Menyu
	path('all_books', all_books, name='all_books'),
	path('bookers', bookers, name='bookers'),
	path('sendM',sendM, name='sendM'),
	path('profile', talaba_tanla, name='profile'),
	path('profile/<id>',talaba, name='talaba'),

	path('contact', contact_m, name='contact_m')
]