from django.shortcuts import redirect

def login_required(func):
    def inner(request,*args, **kwargs):
        if request.session.get('uid'):
            return func(request,*args, **kwargs)
        return redirect('user:login')
    return inner
