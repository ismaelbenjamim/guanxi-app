from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404

from user.forms import AccountConfirmForm, AccountConfirmCodeForm
from user.models import Account


def superuser_required(user):
    return user.is_superuser


@login_required(login_url='login')
@user_passes_test(superuser_required, login_url='dashboard')
def account_list_admin(request):
    accounts = Account.objects.all()
    return render(request, 'dashboard/admin/accounts/list.html', {'accounts': accounts})


@login_required(login_url='login')
@user_passes_test(superuser_required, login_url='dashboard')
def account_create_admin(request):
    if request.method == "POST":
        form = AccountAdminForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.save()
            return redirect('account_list_admin')
    else:
        form = AccountAdminForm()
    return render(request, 'dashboard/admin/accounts/form.html', {'form': form, 'title': 'Criar Conta'})


@login_required(login_url='login')
@user_passes_test(superuser_required, login_url='dashboard')
def account_update_admin(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == "POST":
        form = AccountAdminForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('account_list_admin')
    else:
        form = AccountAdminForm(instance=account)
    return render(request, 'dashboard/admin/accounts/form.html', {'form': form, 'title': 'Editar Conta'})


@login_required(login_url='login')
@user_passes_test(superuser_required, login_url='dashboard')
def account_delete_admin(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == "POST":
        account.delete()
        return redirect('account_list_admin')
    return render(request, 'dashboard/admin/accounts/delete.html', {'account': account})


@login_required(login_url='login')
@user_passes_test(superuser_required, login_url='dashboard')
def account_confirm_admin(request, pk):
    account = get_object_or_404(Account, pk=pk)

    if request.method == "POST":
        if not request.POST.get('code'):
            form = AccountConfirmForm(request.POST, initial={'username': account.username})
            if form.is_valid():
                form.save(account)
                return redirect('account_list_admin')
        else:
            form = AccountConfirmCodeForm(request.POST, account=account)
            if form.is_valid():
                form.save()
                return redirect('account_list_admin')
    else:
        if account.status == account.AccountStatus.WAITING_CODE:
            form = AccountConfirmCodeForm(initial={'username': account.username}, account=account)
        else:
            form = AccountConfirmForm(initial={'username': account.username})

    return render(request, 'dashboard/admin/accounts/confirm.html', {'form': form, 'title': 'Confirmar Conta'})

