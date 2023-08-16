from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import News
from .forms import NewsForm
from django.http import FileResponse, Http404


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('news_main')
    return render(request, template_name='login.html')


def logout_user(request):
    logout(request)
    return redirect('news_main')


def news_main(request):
    news = News.objects.all()
    return render(request, template_name='news_main.html', context={'news': news})


def author_news(request, author_id):
    author = User.objects.get(id=author_id)
    news_of_author = News.objects.filter(author=author)
    return render(request, template_name='author_news.html', context={'author': author, 'news': news_of_author})


@login_required
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('news_main')
    else:
        form = NewsForm
    return render(request, template_name="add_news.html", context={'form': form})


@login_required
def edit_news(request, news_id):
    news_item = News.objects.get(id=news_id)

    if request.method == 'POST':
        form = NewsForm(data=request.POST, files=request.FILES, instance=news_item)
        if form.is_valid():
            form.save()
            return redirect('news_main')
    else:
        form = NewsForm(instance=news_item)
    return render(request, template_name="edit_news.html", context={'form': form})

@login_required
def delete_news(request, news_id):
    news_item = News.objects.get(id=news_id)
    if request.user == news_item.author:
        news_item.delete()
    return redirect('news_main')


def download_file(request, news_id):
    news_item = News.objects.get(id=news_id)
    try:
        return FileResponse(open(news_item.file.path, 'rb'), as_attachment=True)
    except FileNotFoundError:
        raise Http404("File with this name not Found")


