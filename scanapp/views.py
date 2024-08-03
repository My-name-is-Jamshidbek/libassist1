from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
import datetime
from accounts.models import Book, Accept_Book, Students, Return_Book


def scan_view(request):
    if request.method == 'POST':
        barcode = request.POST.get('barcode')

        if Book.objects.filter(key=barcode).exists():
            return redirect('bar_give_book', key=barcode)
        elif Accept_Book.objects.filter(key=barcode).exists():
            if Accept_Book.objects.filter(key=barcode).exists():
                book = Accept_Book.objects.get(key=barcode)
                Return_Book(
                    student=book.student,
                    staff="Avtomat",
                    book_name=book.book_name,
                    author=book.author,
                    date=book.created,
                    respite=book.respite,
                    key=book.key,
                ).save()
                Book(
                    book_name=book.book_name,
                    author=book.author,
                    key=book.key,
                ).save()
                obj = get_object_or_404(Accept_Book, key=barcode)
                obj.delete()
            messages.success(request, 'Kitob qabul qilindi')
        else:
            messages.error(request, 'Inventar raqam topilmadi')

        return redirect('scan')

    return render(request, 'scanapp/scan.html')


def bar_give_book_view(request, key):
    if request.method == 'POST':
        username = request.POST.get('username')
        passcode = request.POST.get('passcode')
        respite = request.POST.get('respite')

        try:
            student = Students.objects.get(admin__username=username)
        except Students.DoesNotExist:
            messages.error(request, 'Foydalanuvchi nomi yoki xavfsizlik kodi noto`g`ri!')
            return redirect('bar_give_book', key=key)

        if str(student.passCode) != str(passcode):
            messages.error(request, 'Foydalanuvchi nomi yoki xavfsizlik kodi noto`g`ri!')
            return redirect('bar_give_book', key=key)

        if Accept_Book.objects.filter(key=key).exists():
            messages.error(request, 'Bu kitob berilgan!')
            return redirect('scan')

        try:
            book = Book.objects.get(key=key)
        except Book.DoesNotExist:
            messages.error(request, 'Bu kitob mavjud emas!')
            return redirect('scan')


        Accept_Book.objects.create(
            student=student,
            staff="Avtomat",
            book_name=book.book_name,
            author=book.author,
            key=book.key,
            respite=timezone.now() + datetime.timedelta(days=int(respite))
        )

        book.delete()
        messages.success(request, 'Kitob berildi')
        return redirect('scan')

    book = get_object_or_404(Book, key=key)
    return render(request, 'scanapp/give.html', {'book': book})
