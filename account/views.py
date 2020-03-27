from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login as login_method, logout as logout_method
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from . models import PasswordResetRequest

def login(req):

    if req.user.is_authenticated: ### Check if user is already logged in
        return HttpResponseRedirect(reverse('dashboard:dashboard'))

    context = {}
    if req.method == 'POST':
        username = req.POST['login-username']
        password = req.POST['login-password']

        user = authenticate(req, username=username, password=password)

        if user:
            login_method(req, user)
            return HttpResponseRedirect(reverse('dashboard:dashboard'))
        else:
            context = {
                'message': 'Username or password are incorrect.'
            }
            
    return render(req, 'login.html', context)

def logout(req):
    logout_method(req)
    return render(req, 'login.html')

def signup(req):

    if req.user.is_authenticated: ### Check if user is already logged in
        return HttpResponseRedirect(reverse('dashboard:dashboard'))

    context = {}
    if req.method == 'POST':

        ### Input values
        firstname = req.POST['first_name']
        lastname = req.POST['last_name']
        username = req.POST['username']
        email = req.POST['email']
        password1 = req.POST['password']
        password2 = req.POST['password_confirm']

        ### Staff registration
        is_staff = req.POST['is_staff']
        staff_token = req.POST['staff_token']
        staff_registration_token = 'zxcvbnm'

        if password1 == password2: ### Check if passwords match
            if User.objects.filter(username=username).exists(): ### Check if user already exists
                context = {
                    'message': 'User already exists'
                }
            else:
                if is_staff == 'staff': ### Check if new user is staff 
                    if staff_token == staff_registration_token: ### Check if staff registration token is correct
                        User.objects.create_superuser(
                            username, email, password1, first_name=firstname, last_name=lastname
                        )
                        context = {
                            'message': 'Staff user has been created! You can now login and access /admin.'
                        }
                    else:
                        context = {
                            'message': 'Staff token was not correct'
                        }
                else:
                    User.objects.create_user(
                        username, email, password1, first_name=firstname, last_name=lastname
                    )
                    context = {
                        'message': 'User has been created! You can now go you the login page and login.'
                    }
        else:
            context = {
                'message': 'Passwords did not match.'
            }
    return render(req, 'signup.html', context)

def request_reset_password(req):
    context = {}
    if req.method == 'POST':
        email = req.POST['reset-email']
        is_email_valid = User.objects.filter(email=email).exists()

        if is_email_valid: ### Check if email exists in our system
            new_request = PasswordResetRequest()
            new_request.email = email
            new_request.save()
            print(new_request) ### This is what should be sent to the users email
            return HttpResponseRedirect(reverse('password_reset'))

        else:
            context = {
                'message': 'The email does not exists in our system'
            }


    return render(req, 'request_reset_password.html', context)

def password_reset(req):
    context = {}

    if req.method == 'POST':
        token = req.POST['pass-reset-token']
        email = req.POST['pass-reset-email']
        password = req.POST['pass-reset-password']
        password_confirm = req.POST['pass-reset-password-confirm']

        if password == password_confirm: ### Check if passwords match
            valid_token = PasswordResetRequest.objects.filter(token=token, active=True).exists()
            valid_user = User.objects.filter(email=email).exists()

            if valid_token and valid_user: ### Check if token exists and is active
                db_token = PasswordResetRequest.objects.get(token=token)
                db_token.active = False
                db_token.save()

                user = User.objects.get(email=email)
                user.set_password(password)
                user.save()

                context = {
                    'success_message': f'Your password has succesfully been changed! Go back to the login page',
                    'message': False
                }
            else:
                context = {
                    'message': 'Invalid token or email.'
                }
        else:
            context = {
                'message': 'Passwords do not match.'
            }

    return render(req, 'password_reset.html', context)

def change_password(req):
    context = {}

    if req.method == 'POST':
        username = req.user.get_username()
        current_password = req.POST['change-current-password']
        new_password = req.POST['change-new-password']
        new_password_confirm = req.POST['change-new-password-confirm']

        if new_password == new_password_confirm: ### Check if new passwords match
            valid_user = authenticate(req, username=username, password=current_password)
            if valid_user: ### Check if current password is correct
                user = User.objects.get(username=username)
                user.set_password(new_password)
                user.save()
                context = {
                    'message': 'Your password has been updated!'
                }
            else:
                context = {
                    'message': 'Current password is wrong.'
                }
        else:
            context = {
                'message': 'Your new password do not match.'
            }

    return render(req, 'change_password.html', context)

def delete_account(req):
    context = {}
    if req.method == 'POST':
        username = req.user.get_username()
        password = req.POST['delete-password']
        text_delete = req.POST['delete-confirm']
        valid_user = authenticate(req, username=username, password=password)
        if valid_user: ### Check if password is correct
            if text_delete == 'delete':
                logout_method(req)
                user = User.objects.get(username=username)
                user.delete()
                return HttpResponseRedirect(reverse('login'))
            else:
                context = {
                    'message': '\'delete\' was not typed correctly.'
                }
        else:
            context = {
                'message': 'Wrong password.'
            }

    return render(req, 'delete_account.html', context)
    