from django.shortcuts import render,redirect
from django.views import View
from django.template.loader import get_template
from .forms import QdForm
from .models import Qd
from clazz.models import Clazz
from user.models import User
import time
from django.core.paginator import Paginator
def get_today():
    return time.strftime('%Y-%m-%d',time.localtime(time.time()))
# Create your views here.
class QdView(View):
    def get(self,request):
        return render(request,'qd/index.html')
    def post(self,request):
        form = QdForm(request.POST)
    
        if form.is_valid():
            user = User.objects.filter(id=request.session['uid']).first()
            Qd.objects.create( 	stage=form.cleaned_data['stage'],
                                progress=form.cleaned_data['progress'],
                                code_num=form.cleaned_data['code_num'],
                                bug_num=form.cleaned_data['bug_num'],
                                remark=form.cleaned_data['remark'],
                                uid = user,
                                create_time = get_today()
                            )
                        
            return render(request,'qd/index.html',{'msg':'签到成功！！'})
        else:
            return render(request,'qd/index.html',{'msg':'签到失败！！'})


class QdList(View):
    def get(self,request):
        if request.session.get('rid'):
            uid = request.session.get('uid')
            qds = Qd.objects.filter(uid=uid).order_by('-create_time')
            paginator = Paginator(qds, 5)
            page = request.GET.get('page')
            pager = paginator.get_page(page)
            return render(request,'qd/list.html',{'data':pager})
        else:
            cname = request.GET.get('cname')
            uname = request.GET.get('uname')
            create_time = request.GET.get('create_time')
            qds = Qd.objects
            if create_time:
                qds = qds.filter(create_time = create_time)
            if uname:
                user = User.objects.filter(nick_name = uname).first()
                qds = qds.filter(uid =user.id)
            if cname:
                clazz = Clazz.objects.filter(name = cname).first()
                uids = [u.id for u in User.objects.filter(clazz = clazz.id).all()]
                qds = qds.filter(uid__in=uids)
            qds = qds.all().order_by('-create_time')
            paginator = Paginator(qds, 5)
            page = request.GET.get('page')
            pager = paginator.get_page(page)
            return render(request,'qd/list_admin.html',{'data':pager})
    def post(self,request):
        pass