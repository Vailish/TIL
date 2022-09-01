from django.shortcuts import render, redirect

from .models import Article

# Create your views here.
def index(request):
    # articles = Article.objects.all()[::-1]  # 이렇게하면 최신글부터 볼 수 있음
    articles = Article.objects.order_by('-pk')  # 큰거부터 나오게 하는거
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    article = Article(title=title, content=content)  # 1번방법
    article.save()

    # article = Article()  # 2번방법
    # article.title = title
    # article.content = content
    # article.save()

    # Article.objects.create(title=title, content=content)  # <-3번방법

    return redirect('articles:index')  # redirect는 경로 우회 저기로가!

def detail(request, pk):
    article = Article.objects.get(pk=pk)  # 오른쪽이 인자값
    context = {
        'article': article,
    }
    return render(request,'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)