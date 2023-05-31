from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login as authlogin, logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser



# Create your views here.
def login(request):
    # user = CustomUser.objects.create_user(first_name="first_name",
    #                                       last_name="last_name",
    #                                       username="username_admin",
    #                                       password="pa-_ssword_/admin.%|.",
    #                                       user_type=1)
    # user.admin.address = "adress"
    # user.save()
    message = ""
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user != None:
            authlogin(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect(reverse('superadmin'))
            elif user.user_type == "2":
                return HttpResponseRedirect(reverse("staff"))
            else:
                return HttpResponseRedirect(reverse("student_profile"))
        else:
            message = "Parol yoki username xato!"
            messages.error(request, message)
    return render(request, 'accounts/login.html', {'message': message})


def log_out(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def contact_s(request):
    context = {
        'employee': []
    }
    return render(request, 'accounts/contact.html', context)
