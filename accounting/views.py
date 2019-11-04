from django.shortcuts import redirect, render
from django.http import HttpResponse

def redirection(request):
    page = ''

    if request.user.is_authenticated:
        page = 'accounting_system:index'
    else:
        page = 'login'

    return redirect(page)
