from django.http import HttpResponse
from django.shortcuts import render

from stuapp.models import Student, Studentpic


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        sname = request.POST.get('sname', '')
        spwd = request.POST.get('spwd', '')
        if sname and spwd:
            stu = Student(sname=sname, spwd=spwd)
            stu.save()
            print('注册成功，跳转至 login.html')
            return render(request, 'login.html')
        return HttpResponse('Failed')


def showinfo(request):
    stu_info = Student.objects.all()
    print(stu_info)
    return render(request, 'showinfo.html', {'stu': stu_info})


def login(request):

    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        sname = request.POST.get('sname', '')
        spwd = request.POST.get('spwd', '')
        result = Student.objects.filter(sname=sname, spwd=spwd)
        print(result)
        if result:
            return HttpResponse('登录成功')
        return HttpResponse('登陆失败')


def pic(request):

    if request.method == 'GET':
        return render(request, 'pic.html')
    else:
        sname = request.POST.get('sname', '')
        spic = request.FILES.get('spic', '')
        info_obj = Studentpic.objects.create(sname=sname, pic=spic)
        if info_obj:
            return HttpResponse('注册成功')
        return HttpResponse('注册失败')


def showpic(request):

    stuinfo = Studentpic.objects.all()
    return render(request, 'showpic.html', {'stuinfo': stuinfo})


def setcookie(request):

    resp = HttpResponse()
    resp.set_cookie('iam', 'cookie')

    return resp


def getcookie(request):

    cookie = request.COOKIES.get('iam')
    return HttpResponse(cookie)