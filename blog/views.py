from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogPost
# Create your views here.

def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs': blogs, 'posts': posts})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'details':details})

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.delete()
    return redirect('home')

def create(request):
    if request.method =='POST': #입력된 내용을 처리해주는 기능
        form = BlogPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')
    else:   #빈페이지를 띄워주는 기능
        form = BlogPost()
        return render(request,'create.html',{'form':form})

def update(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)

    if request.method == 'POST':
        form = BlogPost(request.POST, request.FILES, instance = blog)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = BlogPost(instance = blog)
        return render(request, 'create.html', {'form':form})

##form사용 안한 함수
# def create(request):
#     if request.method == 'POST':
#         blog = Blog()   #Blog모델의 내용들을 blog라는 변수에 담고
#         blog.title = request.POST['title']
#         blog.photo = request.FILES['photo']
#         blog.body = request.POST['body']
#         blog.pub_date = timezone.datetime.now()
#         blog.save()
#         return redirect('/blog/' + str(blog.id))    #redirect는 '요청이 들어오면 저쪽 url로 보내버려'
#     else:
#         return render(request, 'create.html')       #render는 '요청이 들어오면 이 html 파일을 보여줘'

# def update(request, blog_id):
#     blog = get_object_or_404(Blog, pk = blog_id)
#     if request.method == 'POST':
#         blog.title = request.POST['t']
#         # blog.photo = request.FILES['p']
#         blog.body = request.POST['b']
#         blog.save()
#         return redirect('/blog/' + str(blog_id))
#     else:
#         return render(request, 'update.html', {'update':update})    