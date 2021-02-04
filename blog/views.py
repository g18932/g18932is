from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from .models import Post
from .models import Post2
from .models import Post3
from .models import Post4
from .models import Post5
from .models import Chatpost
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_list2(request):
    post2s = Post2.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list2.html', {'post2s': post2s})

def post_detail2(request, pk):
    post2 = get_object_or_404(Post2, pk=pk)
    return render(request, 'blog/post_detail2.html', {'post2':post2})

def post_list3(request):
    post3s = Post3.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list3.html', {'post3s': post3s})

def post_detail3(request, pk):
    post3 = get_object_or_404(Post3, pk=pk)
    return render(request, 'blog/post_detail3.html', {'post3':post3})
         
def post_list4(request):
    post4s = Post4.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list4.html', {'post4s': post4s})

def post_detail4(request, pk):
    post4 = get_object_or_404(Post4, pk=pk)
    return render(request, 'blog/post_detail4.html', {'post4':post4})

def post_list5(request):
    post5s = Post5.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list5.html', {'post5s': post5s})

def post_detail5(request, pk):
    post5 = get_object_or_404(Post5, pk=pk)
    return render(request, 'blog/post_detail5.html', {'post5':post5})
         
def course(request):
    context = {
        'post': Post.objects.all(),
        'post2': Post2.objects.all(),
        'post3': Post3.objects.all(),
        'post4': Post4.objects.all(),
        'post5': Post5.objects.all(),
        
    }
    return render(request, 'blog/course.html', context)

def week_top(request):
    context = {
        'post': Post.objects.all(),
        'post2': Post2.objects.all(),
        'post3': Post3.objects.all(),
        'post4': Post4.objects.all(),
        'post5': Post5.objects.all(),
        
    }
    return render(request, 'blog/week_top.html', context)

def index(request):

    return render(request, 'blog/index.html')

def today_top(request):
    context = {
        'post': Post.objects.all(),
        'post2': Post2.objects.all(),
        'post3': Post3.objects.all(),
        'post4': Post4.objects.all(),
        'post5': Post5.objects.all(),
    }
    return render(request, 'blog/today_top.html',context)

def select(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.isregi()
    return render(request, 'blog/select.html', {'post':post})

def delete(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.notregi()
    return render(request, 'blog/delete.html', {'post':post})

def select2(request,pk):
    post2 = get_object_or_404(Post2,pk=pk)
    post2.isregi()
    return render(request, 'blog/select.html', {'post2':post2})

def delete2(request,pk):
    post2 = get_object_or_404(Post2,pk=pk)
    post2.notregi()
    return render(request, 'blog/delete.html', {'post2':post2})

def select3(request,pk):
    post3 = get_object_or_404(Post3,pk=pk)
    post3.isregi()
    return render(request, 'blog/select.html', {'post3':post3})

def delete3(request,pk):
    post3 = get_object_or_404(Post3,pk=pk)
    post3.notregi()
    return render(request, 'blog/delete.html', {'post3':post3})

def select4(request,pk):
    post4 = get_object_or_404(Post4,pk=pk)
    post4.isregi()
    return render(request, 'blog/select.html', {'post4':post4})

def delete4(request,pk):
    post4 = get_object_or_404(Post4,pk=pk)
    post4.notregi()
    return render(request, 'blog/delete.html', {'post4':post4})

def select5(request,pk):
    post5 = get_object_or_404(Post5,pk=pk)
    post5.isregi()
    return render(request, 'blog/select.html', {'post5':post5})

def delete5(request,pk):
    post5 = get_object_or_404(Post5,pk=pk)
    post5.notregi()
    return render(request, 'blog/delete.html', {'post5':post5})

def today_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/today_detail.html', {'post':post})

def chat_top(request):
    context = {
        'post': Post.objects.all(),
        'post2': Post2.objects.all(),
        'post3': Post3.objects.all(),
        'post4': Post4.objects.all(),
        'post5': Post5.objects.all(),
    }
    return render(request, 'blog/chat_top.html',context)
def chat_list(request, pk):
    chatposts = Chatpost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/chat_list.html', {'chatposts': chatposts, 'post':post})

def chat_detail(request, pk):
    chatpost = get_object_or_404(Chatpost, pk=pk)
    return render(request, 'blog/chat_detail.html', {'chatpost': chatpost})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            chatpost = form.save(commit=False)
            chatpost.author = request.user
            chatpost.published_date = timezone.now()
            chatpost.save()
            return redirect('chat_detail', pk=chatpost.pk)
    else:
        form = PostForm()
    return render(request, 'blog/chat_edit.html', {'form': form})

def add_comment_to_post(request, pk):
    chatpost = get_object_or_404(Chatpost, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment1 = form.save(commit=False)
            comment1.chatpost = chatpost
            comment1.author = request.user
            comment1.save()
            return redirect('chat_detail', pk=chatpost.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


def syllabus(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/syllabus.html', {'post':post})
         
