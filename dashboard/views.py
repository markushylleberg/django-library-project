from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from addmaterial.models import Addmaterial
import datetime


@login_required(login_url='/account/login/')
def dashboard(req):
    context = {
        'materials': Addmaterial.objects.all().order_by('title'),
        'type': 'books or magazines',
        'response': 'Books and magazines',
    }
    return render(req, 'dashboard.html', context)

@login_required(login_url='/account/login/')
def books(req):
    context = {
        'materials': Addmaterial.objects.filter(material_type='book').order_by('title'),
        'type': 'books',
        'response': 'Books',
    }
    return render(req, 'dashboard.html', context)

@login_required(login_url='/account/login/')
def magazines(req):
    context = {
        'materials': Addmaterial.objects.filter(material_type='magazine').order_by('title'),
        'type': 'magazines',
        'response': 'Magazines'
    }
    return render(req, 'dashboard.html', context)

@login_required(login_url='/account/login/')
def my_loans(req):
    context = {}
    return render(req, 'my_loans.html', context)

@login_required(login_url='/account/login/')
def expired_loans(req):
    context = {
        'date': datetime.date.today()
    }
    is_user_staff = req.user.is_staff
    if is_user_staff: ### Check if user is staff member
        pass
    else:
        return HttpResponseRedirect(reverse('dashboard:dashboard'))

    return render(req, 'expired_loans.html', context)
