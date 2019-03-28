from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from stuloginapp.models import registerOper, Clazz,Student


def register(request):

    if request.method == 'GET':
        return render(request, 'stulogin.html')
    elif request.method == "POST":
        sname = request.POST.get('sname')
        clazz = request.POST.get('clazz')
        coursenames = request.POST.getlist('coursename')
        flag = registerOper(sname, clazz, coursenames)
        if flag:
            return HttpResponse('注册成功')
        return HttpResponse('注册失败')
    else:
        return HttpResponse('暂不支持的请求方式')


def showall(request):

    clslist = Clazz.objects.all()
    return render(request, 'showall.html', {'clslist': clslist})


def getstu(request):

    cname = request.GET.get('cname', '')
    stulist = Clazz.objects.get(cname=cname).students.all()

    return render(request, 'stuinfo.html', {'stulist': stulist})
