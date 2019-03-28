from django.shortcuts import render

# Create your views here.
from movieapp.models import TMovie
import math


def page_movie(num, size=12):
    # 1.判断num是否越界
    if num < 1:
        num = 1

    # 获取总页数
    totalRecords = TMovie.objects.count()
    totalPages = math.ceil(totalRecords/size)

    if num > totalPages:
        num = totalPages


    # 1.查询Movie表中所有数据
    movieList = TMovie.objects.all()
    print(type(movieList))
    print(movieList)
    per_page_list = movieList[(num-1)*size:(num*size)]

    return per_page_list, num


def showmovie(request):
    # 接收请求参数
    num = request.GET.get('num', 1)
    num = int(num)

    """ 展示影片信息"""
    per_movie_list, n = page_movie(num)
    previous_page_number = n - 1

    next_page_number = n + 1

    return render(request, 'movie.html', {'movies': per_movie_list,
                                          'previous_page_number': previous_page_number,
                                          'next_page_number': next_page_number})

from django.core.paginator import Paginator


def djangopage(request):
    # 获取当前页码
    page_num = int(request.GET.get('num', 1))
    # 获取数据库数据
    tmovies = TMovie.objects.all().order_by('id')
    # 每一页要显示的资源
    page_obj = Paginator(object_list=tmovies, per_page=12)
    page_data = page_obj.page(page_num)

    start = page_num - math.ceil(10/2)

    if start < 1:
        start = 1

    end = start + 9

    if end > page_obj.num_pages:
        end = page_obj.num_pages

    if end < 10:  # 如果数据库的数据少于10页
        start = 1
    else:
        start = end - 9
    page_num_list = range(start, end+1)

    return render(request, 'movie.html', {'movies': page_data, 'page_num_list': page_num_list, 'page_obj': page_obj})















