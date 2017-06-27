from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.admin.views.decorators import staff_member_required
from django.db import IntegrityError

@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')


def show_login(request):
    if request.method == "GET":
        return render(request, "users/login.html")
    else:
        context = make_login(request)

        if context.get('is_logged'):
            return HttpResponseRedirect(reverse("users:dashboard"))
        else:
            return render(request, "users/login.html", context)

@login_required
def logout_view(request, *args, **kwargs):

    return logout(request, *args, **kwargs)

def make_login(request):
    form = request.POST
    username = form.get('username')
    password = form.get('password')

    user = authenticate(username=username, password=password)
    is_logged = False

    if user is not None:
        login(request, user)
        message = "Logged"

        is_logged = True
    else:
        message = "Incorrect user"

    context = {
        "is_logged": is_logged,
        "message": message,
    }

    return context

def fullValidation(form):
    first_name = form.get('first_name')
    last_name = form.get('last_name')
    email = form.get('email')
    original_email = form.get('original_email')

    resultCheck = ''
    resultCheck += check_name(first_name, last_name)
    resultCheck += check_email(email)
    resultCheck += check_email_exist(email, original_email)

    return resultCheck


def fullValidationRegister(form, user=None):
    currentPassword = form.get('currentPassword')
    password = form.get('password')
    confirmPassword = form.get('confirmPassword')

    resultCheck = ''
    if user is not None:
        resultCheck += check_current_password(user, currentPassword)
        resultCheck += check_password_lenght(password, confirmPassword)
        resultCheck += check_password(password, confirmPassword)

    return resultCheck

def check_name(first_name, last_name):
    if not first_name.isalpha() or not last_name.isalpha():
        return 'Nome deve conter apenas letras'
    else:
        return ''


def check_email(email):
    if '@' not in email or '.' not in email or ' ' in email:
        return 'Email invalido'
    else:
        return ''


def check_email_exist(email, original_email):
    if User.objects.filter(email=email).exists() and email != original_email:
        return ' -- E-mail ja esta cadastrado no nosso banco de dados'
    else:
        return ''


def check_password_lenght(password, confirmPassword):
    if len(password) < 6 and password != confirmPassword:
        return ' -- Senha Invalida, digite uma senha com no minimo 6 letras'
    else:
        return ''


def check_password(password, confirmPassword):
    if password != confirmPassword:
        return ' -- Senha invalida! Senhas de cadastros diferentes'
    else:
        return ''


def check_current_password(user, currentPassword):

    if not user.check_password(currentPassword):
        return ' -- Campo de Senha atual diferente da Senha Atual!'
    else:
        return ''


@login_required
def self_edit_user(request):

    user = User.objects.get(pk=request.user.id)

    if request.method == "GET":
        return render(request, 'users/self_edit.html',)

    else:
        form = request.POST
        first_name = form.get('first_name')
        last_name = form.get('last_name')
        # email = form.get('email')
        email = request.user.username

        resultCheck = fullValidationRegister(form)
        resultCheck += fullValidation(form)

        user.first_name = first_name
        user.last_name = last_name
        user.username = email
        user.email = email
        user.save()

        # login(request,user)
        update_session_auth_hash(request, user)

        return render(request, 'users/dashboard.html')

@staff_member_required
def register(request):

    if request.method == "GET":
        return render(request, 'users/create_user.html')
    else:
        form = request.POST
        first_name = form.get('first_name')
        last_name = form.get('last_name')
        password = form.get('password')
        confirmPassword = form.get('confirmPassword')
        email = form.get('email')
        user_type = form.get('user_type')

        resultCheck = fullValidationRegister(form)
        resultCheck += fullValidation(form)

        if len(resultCheck) != 0:
            return render(
                request,
                'users/create_user.html',
                {'falha': resultCheck})

        try:
            if user_type == 'common':
                user = User.objects.create_user(first_name=first_name,
                                                last_name=last_name,
                                                password=password,
                                                username=email)
            else:
                user = User.objects.create_superuser(first_name=first_name,
                                                     last_name=last_name,
                                                     password=password,
                                                     username=email,
                                                     email=email)

        except IntegrityError as e:
            return render(request, 'users/create_user.html',
                          {'falha': 'Invalid email, email already exist'})
        except:
            return render(request, 'users/create_user.html',
                          {'falha': 'unexpected error'})

        user.save()
        messages.success(request, 'Usuario registrado com sucesso')


    return render(request, 'users/dashboard.html')


@staff_member_required
def list_user_edit(request):
    return __list__(request, 'users/list_user_edit.html')

@staff_member_required
def list_user(request):
    return __list__(request, 'users/list_user.html')

def __list__(request, template):

    users = User.objects.all()

    return render(request, template, {'users': users})

def __prepare_error_render__(request, fail_message, user):

    return render(request, 'userEdit/editUsers.html',
                  {'falha': fail_message, 'user': user})


def __prepare_error_render_self__(request, fail_message, user):

    return render(request, 'users/change_password.html',
                  {'falha': fail_message, 'user': user})



def check_permissions(user):
    context = {
        'user': user,
    }
    return context

@staff_member_required
def edit_user(request, user_id):

    user = User.objects.get(id=user_id)

    if request.method == "GET":
        context = check_permissions(user)
        return render(request, 'users/edit_user.html', context)

    else:
        form = request.POST
        first_name = form.get('first_name')
        last_name = form.get('last_name')
        email = form.get('email')
        user_type = form.get('user_type')
        resultCheck = fullValidation(form)

        if len(resultCheck) != 0:
            return __prepare_error_render__(request, resultCheck, user)

        user.first_name = first_name
        user.last_name = last_name
        user.username = email
        user.email = email

        if user_type == 'common':
            user.is_superuser = False
        else:
            user.is_staff = True


        context = check_permissions(user)
        user.save()
        context['info'] = 'usuario modificado com sucesso'

        return render(request, 'users/edit_user.html', context)


def __list__(request, template):

    users = User.objects.all()

    return render(request, template, {'users': users})
