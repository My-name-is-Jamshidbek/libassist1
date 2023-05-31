from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from accounts.models import Group, Return_Book, Students, EmplayeeMessages, Accept_Book, Book
from django.db.models import Count

def staff_context():
    context = {
        # 'group': Group.objects.all().count,
        'accept': Accept_Book.objects.all().count(),
        # 'sms': EmplayeeMessages.objects.all(),
        # 'data': timezone.now(),
        # 'null': Students.objects.filter(return_book__isnull=True).count(),
        # 'good': Students.objects.all().count() - Students.objects.filter(return_book__isnull=True).count(),
        'students_count': Students.objects.all().count(),
        'books_count': Book.objects.all().count(),
        'bookers': Students.objects.annotate(num=Count('return_book')).order_by('-num')[:12],
    }
    return context

@login_required(login_url='login')
def staff_xizmatlar(request):
    return render(request, 'staff/home/xizmatlar.html', staff_context())


@login_required(login_url='login')
def staff_sozlamalar(request):
    return render(request, 'staff/home/sozlamalar.html', staff_context())



@login_required(login_url='login')
def staff(request):
    return render(request, 'staff/home/staff.html', staff_context())
