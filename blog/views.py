from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import NewBlog

# Create your views here.

def index(request):
    blog = Blog.objects
    #블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return해 준다
    posts = paginator.get_page(page)
    return render(request, 'blog/index.html', {'blog':blog, 'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog_detail})

def create(request):
    return render(request, 'blog/create.html')

def new1(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/detail/' +str(blog.id))

def update1(request, pk): # 수정페이지 다시 할것
    blog = get_object_or_404(Blog, pk)
    form = NewBlog(request.POST, instance=Blog)
    if form.is_valid():
        form.save()
        return redirect('/detail/' +str(blog.id))
    return render(request, 'blog/index.html')
    
def delete1(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('index')