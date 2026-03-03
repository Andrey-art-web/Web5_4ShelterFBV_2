# from django.shortcuts import render, reverse, redirect
# from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth import authenticate, login, logout
#
# from users.forms import UserRegisterForm, UserLoginForm, UserUpdateForm
#
# def user_register_view(request):
#     if request.method == "POST":
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             new_user = form.save()
#             # print(new_user)
#             # print(form.cleaned_data['password'])
#             new_user.set_password(form.cleaned_data['password'])
#             new_user.save()
#             return HttpResponseRedirect(reverse('users:user_login'))
#     context = {
#         'title': 'Создать аккаунт',
#         'form': UserRegisterForm
#     }
#
#     return render(request, 'users/user_register.html', context=context)
#
#
# def user_login_view(request):
#     if request.method == "POST":
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(email=cd['email'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponseRedirect(reverse('dogs:index'))
#                 else:
#                     return HttpResponse('Аккаунт неактивен !')
#     context = {
#         'title': 'Авторизация',
#         'form': UserLoginForm
#     }
#
#     return render(request, 'users/user_login.html', context=context)

## если в БД нет значений по умолчанию
# def user_profile_view(request):
#     user_object = request.user
#     if user_object.first_name and user_object.last_name:
#         user_name = user_object.first_name + ' ' + user_object.last_name
#     else:
#         user_name = "Anonymous"
#     context = {
#         'title': f'Ваш профиль {user_name}'
#     }
#     return render(request, 'users/user_profile_read_only.html', context=context)

# def user_profile_view(request):
#     user_object = request.user
#     context = {
#         'title': f'Ваш профиль {user_object}'
#     }
#     return render(request, 'users/user_profile_read_only.html', context=context)
#
#
# def user_logout_view(request):
#     logout(request)                    # 1. Завершает сессию пользователя
#     return redirect('dogs:index')       # 2. Перенаправляет на главную страницу
#
#
# from django.shortcuts import render, HttpResponseRedirect
# from django.urls import reverse
#
#
# def user_update_view(request):
#     user_object = request.user
#     if request.method == 'POST':
#         form = UserUpdateForm(request.POST, request.FILES, instance=user_object)
#         if form.is_valid():
#             user_object = form.save()
#             user_object.save()
#             return HttpResponseRedirect(reverse('users:user_profile'))
#             context = {
#         'object': user_object,
#         'title': f'Изменить профиль {user_object}',
#         'form': UserUpdateForm(instance=user_object)
#     }
#     return render(request, 'users/user_update.html', context)

from django.shortcuts import render, reverse, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from users.forms import UserRegisterForm, UserLoginForm, UserUpdateForm


def user_register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect(reverse('users:user_login'))
    else:
        form = UserRegisterForm()

    context = {
        'title': 'Создать аккаунт',
        'form': form,
    }

    return render(request, 'users/user_register_update.html', context)


def user_login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('dogs:index'))
                else:
                    return HttpResponse('Аккаунт неактивен !')
    else:
        form = UserLoginForm()

    context = {
        'title': 'Авторизация',
        'form': form,
    }

    return render(request, 'users/user_login.html', context)


def user_profile_view(request):
    user_object = request.user

    if not user_object.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))

    context = {
        'title': f'Ваш профиль {user_object.email}',
        'object': user_object,
    }
    return render(request, 'users/user_profile_read_only.html', context)


def user_logout_view(request):
    logout(request)
    return redirect('dogs:index')


def user_update_view(request):
    user_object = request.user

    if not user_object.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user_object)
        if form.is_valid():
            user_object = form.save()
            return HttpResponseRedirect(reverse('users:user_profile'))
    else:
        form = UserUpdateForm(instance=user_object)

    context = {
        'object': user_object,
        'title': f'Изменить профиль {user_object.email}',
        'form': form,
    }

    return render(request, 'users/user_register_update.html', context)
