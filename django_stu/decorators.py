from django.shortcuts import redirect
from functools import wraps
def login_required(func):
    def inner(request,*args, **kwargs):
        if request.session.get('uid'):
            return func(request,*args, **kwargs)
        return redirect('user:login')
    return inner




