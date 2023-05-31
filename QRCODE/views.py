from django.utils import timezone
import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from accounts.models import Group, Return_Book, Staffs, Students, Book, Accept_Book, Check
from library.staff import staff
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
# Create your views here.
def main(request, id):          
    if Accept_Book.objects.filter(key=id).exists():
        book_data = Accept_Book.objects.get(key=id)
        context = {
            "book_data": book_data,
            'id': id,
        }
        return render(request, 'qrcode/return.html', context)
    elif Book.objects.filter(key=id).exists():
        book_data = Book.objects.get(key=id)
        goups = Group.objects.all()
        if request.method == 'POST':
            try:
                group_id = request.POST['group']
                student = request.POST['student']
                respite = request.POST['respite']
                group = Group.objects.filter(id=group_id)
                if group_id!='nan' and student=="nan":
                    students = Students.objects.filter(groups__id=group_id)
                    context = {
                        "book_data": book_data,
                        "groups": goups,
                        "students": students,
                        "changed_group_value": group_id,
                        "changed_group_name": group[0],
                        'id': id,
                    }
                    return render(request, 'qrcode/give.html', context)
                elif group!="nan" and student!="nan":
                    book_key = id
                    id = Students.objects.get(id=student)

                    staff_id = request.user.id
                    if Book.objects.filter(key=book_key).exists():
                        if Accept_Book.objects.filter(book_name=Book.objects.get(key=book_key).book_name).exists():
                            messages.success(request, 'Bu kitob berilgan!')
                        else:
                            Accept_Book(
                                student=id,
                                staff=Staffs.objects.get(admin=staff_id).admin.username,
                                book_name=Book.objects.get(key=book_key).book_name,
                                author=Book.objects.get(key=book_key).author,
                                key=Book.objects.get(key=book_key).key,
                                respite=timezone.now() + datetime.timedelta(days=int(respite))
                            ).save()
                            obj = get_object_or_404(Book, id=Book.objects.get(key=book_key).id)
                            obj.delete()
                            messages.success(request, 'Kitob berildi')
                        return redirect('main', book_key)
                    else:
                        messages.success(request, "Bu Raqamli kitob bazada yo'q?")
            except Exception as _:
                messages.success(request, "Ma'lumotlar to'ldirilmagan!!")
        students = Students.objects.all()
        context = {
            "book_data": book_data,
            "groups": goups,
            "students": students,
            "changed_group_value": "nan",
            "changed_group_name": "Guruh tanlash",
            'id': id,
        }
        return render(request, 'qrcode/give.html', context)
    else:
        return render(request, 'qrcode/no.html')

@login_required(login_url='login')
def return_book(request, id):
    if Accept_Book.objects.filter(key = id).exists():
        a = Accept_Book.objects.get(key=id).student
        Return_Book(student=Students.objects.get(id=a.id),
            staff = Staffs.objects.get(admin=request.user.id).admin.username,
            book_name=Accept_Book.objects.get(key=id).book_name,
            author=Accept_Book.objects.get(key=id).author,
            respite=Accept_Book.objects.get(key=id).respite,
            date=timezone.now(),
            key=Accept_Book.objects.get(key=id).key,
            ).save()
        Book(
            book_name=Accept_Book.objects.get(key=id).book_name,
            author=Accept_Book.objects.get(key=id).author,
            key=Accept_Book.objects.get(key=id).key,
            ).save()
        obj = get_object_or_404(Accept_Book, key=id)
        obj.delete()
        return redirect("main", id)
    else:
        return render(request, 'qrcode/no.html')
