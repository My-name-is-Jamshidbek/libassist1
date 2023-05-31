from datetime import timezone
import datetime
from django.shortcuts import get_object_or_404, redirect, render
from accounts.models import Accept_Book, Book, Students, SendMessages, Group, Return_Book
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='login')
def all_books(request):
    if request.method == 'POST':
        search = request.POST['search']
        book = Book.objects.filter(book_name__contains=search)
        context = {
        'book': book[:100],
        }
        return render(request, 'staff/all_book.html', context)
    else:
        context = {
            'book': Book.objects.all()[:100],
            }
        return render(request, 'staff/all_book.html', context)


@login_required(login_url='login')
def bookers(request):
    stat = Students.objects.annotate(num=Count('return_book')).order_by('-num')
    return render(request, 'staff/statistics.html', {'statistics': stat, 'student': Students.objects.all()})


@login_required(login_url='login')
def sendM(request):
    if request.method == 'POST':
        name = request.user
        title = request.POST['title']
        body = request.POST['message']
        try:
            SendMessages(name=name, title=title, body=body).save()
            return redirect('sendM')
        except:
            messages.success('yuborib bo\'lmadi')
    return render(request,'staff/sendMessages.html')


def talaba_tanla(request):
    if request.method == 'POST':
        group = request.POST['group']
        member = Students.objects.filter(groups=group)
        context = {
            'member': member,
            'g':Group.objects.get(id=group).number,
            'group': Group.objects.all(),
        }
        return render(request, 'staff/profile_talaba.html', context)
    return render(request, 'staff/profile_talaba.html', {'group': Group.objects.all()})


def talaba(request, id):
    student = Students.objects.get(id=id)
    context = {
        'student': student,
        'acceptbook': Accept_Book.objects.filter(student=id),
        'return_book': Return_Book.objects.filter(student=id),
    }
    return render(request, 'staff/talaba.html', context)



@login_required(login_url='login')
def contact_m(request):
    context = {
        'employee': []
    }
    return render(request, 'staff/contact.html', context)
