from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from .models import Loan
from addmaterial.models import Publishmaterial, Addmaterial
from datetime import datetime, timedelta

@login_required(login_url='/account/login/')
def new_loan(req):
    if req.method == 'POST':
        user_id = req.user
        book_post = req.POST['material_id']
        data_post = req.POST['material_data']
        # book_id = Publishmaterial.objects.filter(pk=req.POST['material_pk'])
        book_id = Publishmaterial.objects.filter(id=book_post)
        book_data = Addmaterial.objects.filter(id=data_post)

        ### Check if user has more than 10 books || 3 magazines loaned already
        current_book_loans_amount = Loan.objects.filter(user=req.user, is_returned=False, book_id__material_id__material_type='book').count()
        current_magazine_loans_amount = Loan.objects.filter(user=req.user, is_returned=False, book_id__material_id__material_type='magazine').count()

        if current_book_loans_amount == 10 and current_magazine_loans_amount == 3:
            print('The user has reached the maximum loan amount of books and magazines.')
        else:
            if book_data[0].material_type == 'magazine' and current_magazine_loans_amount == 3 or book_data[0].material_type == 'book' and current_book_loans_amount == 10:
                print('The user has reached the maximum of either books or magazines.')
            else:
                ### Check if user has expired material - if they have -> deny loan
                current_date = datetime.now()

                does_user_have_expired_material = Loan.objects.filter(user=user_id, loan_return_datetime__lt=current_date, is_returned=False).exists()
                if does_user_have_expired_material:
                    print('User has expired material! The user cannot loan more before returnin the expired material.')
                else:
                    ### APPROVED ( NO MAXIMUM AMOUNT OF LOAN ALREADY || NO EXPIRED MATERIAL ) :
                    ### Define the return date
                    current_date = datetime.now()

                    if book_data[0].material_type == 'magazine':
                        return_date = current_date+timedelta(days=7)
                    else:
                        return_date = current_date+timedelta(days=30)

                    new_loan = Loan()
                    new_loan.user = user_id
                    new_loan.book_id = book_id[0]
                    new_loan.loan_return_datetime = return_date
                    new_loan.save()

                    ### Change status to is_loaned = True on given published material
                    book_loaned = Publishmaterial.objects.get(id=book_post)
                    book_loaned.is_loaned = True
                    book_loaned.save()

        return HttpResponseRedirect(reverse('dashboard:dashboard'))

@login_required(login_url='/account/login/')
def return_loan(req):
    if req.method == 'POST':
        user_id = req.user
        loan_id = req.POST['loan_id']
        loan_data = Loan.objects.filter(id=loan_id)[0]

        if user_id == loan_data.user:  ### Check if this is actually a loan that the logged in user has made
            ### Change status in loan
                loan_data.is_returned = True
                loan_data.save()
            ### Change status on published item
                loan_published_material_id = loan_data.book_id.id
                loan_published_material = Publishmaterial.objects.filter(id=loan_published_material_id)[0]
                loan_published_material.is_loaned = False
                loan_published_material.save()
        else:
            print('This is not a loan that the authenticated user has made.')

    return HttpResponseRedirect(reverse('dashboard:my_loans'))
