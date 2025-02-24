from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from user.forms import CustomAuthenticationForm, RegisterForm, AccountForm, AccountConfirmForm, AccountConfirmCodeForm
from user.models import Account


def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Credenciais inválidas.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Por favor, corrija os erros abaixo.")
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def account_list(request):
    accounts = Account.objects.filter(user=request.user)
    return render(request, 'dashboard/accounts/list.html', {'accounts': accounts})


@login_required(login_url='login')
def account_create(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()
            return redirect('account_list')
    else:
        form = AccountForm()
    return render(request, 'dashboard/accounts/form.html', {'form': form, 'title': 'Criar Conta'})


@login_required(login_url='login')
def account_update(request, pk):
    account = get_object_or_404(Account, pk=pk, user=request.user)
    if request.method == "POST":
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = AccountForm(instance=account)
    return render(request, 'dashboard/accounts/form.html', {'form': form, 'title': 'Editar Conta'})


@login_required(login_url='login')
def account_delete(request, pk):
    account = get_object_or_404(Account, pk=pk, user=request.user)
    if request.method == "POST":
        account.delete()
        return redirect('account_list')
    return render(request, 'dashboard/accounts/delete.html', {'account': account})


@login_required(login_url='login')
def account_confirm(request, pk):
    account = get_object_or_404(Account, pk=pk, user=request.user)

    if request.method == "POST":
        if not request.POST.get('code'):
            form = AccountConfirmForm(request.POST, initial={'username': account.username})
            if form.is_valid():
                form.save(account)
                return redirect('account_list')
        else:
            form = AccountConfirmCodeForm(request.POST, account=account)
            if form.is_valid():
                form.save()
                return redirect('account_list')
    else:
        if account.status == account.AccountStatus.WAITING_CODE:
            form = AccountConfirmCodeForm(initial={'username': account.username}, account=account)
        else:
            form = AccountConfirmForm(initial={'username': account.username})

    return render(request, 'dashboard/accounts/confirm.html', {'form': form, 'title': 'Confirmar Conta'})
