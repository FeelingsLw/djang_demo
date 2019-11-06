from django.shortcuts import render,redirect
from django.views import View
from django.template.loader import get_template
from .forms import QdForm
from .models import Qd
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
        qds = Qd.objects.all().order_by('-create_time')
        paginator = Paginator(qds, 1)
        page = request.GET.get('page')
        pager = paginator.get_page(page)
        return render(request,'qd/list.html',{'data':pager})
    def post(self,request):
        pass