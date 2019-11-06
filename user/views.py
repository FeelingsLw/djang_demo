from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from user.models import User
from clazz.models import Clazz
from django.views import View
# Create your views here.


def login(request):
    msg = None
    if 'POST' == request.method:
        # 获取从前台传来的uname
        uname = request.POST.get('uname')
        # 获取从前台传来的pwd
        pwd = request.POST.get('pwd')
        # 用前台传来的uname与pwd 去数据库中 匹配数据，因只要有一条匹配上就可以登录所以使用first()
        user = User.objects.filter(uname=uname, pwd=pwd).first()
        # 判断从数据库获取到数据
        if user:
            request.session['uid'] = user.id
            request.session['nick_name'] = user.nick_name
            # 获取到数据后跳转主页
            return render(request, 'index.html')
        # 获取不到数据设置错误信息
        msg = '用户名或密码错误！'
    # GET请求与登录错误时跳转登录页面
    return render(request, 'login.html', {'msg': msg})

def logout(request):
    request.session.clear()
    return redirect('user:login')

class RegisterView(View):
    def get(self,request):
        clazzs = Clazz.objects.all()
        return render(request,'register.html',{'clazzs':clazzs})
    def post(self,request):
        # 获取从前台传来的uname
        uname = request.POST.get('uname')
        # 获取从前台传来的nick_name
        nick_name = request.POST.get('nick_name')
        # 获取从前台传来的phone
        phone = request.POST.get('phone')
        # 获取从前台传来的sex
        sex = 1 if request.POST.get('sex') == '女' else 0
        # 获取从前台传来的pwd
        pwd = request.POST.get('pwd')
        # 获取从前台传来的cid
        cid = request.POST.get('cid')
        # 通过CID获取clazz的对象
        clazz = Clazz.objects.filter(id=cid).first()
        user = User.objects.create(uname=uname,nick_name=nick_name,phone=phone,sex =sex,pwd=pwd,clazz=clazz)
        # 跳转到登录页面
        return redirect(reverse('user:login'))