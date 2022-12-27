from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# 디버깅용, 예시를 위해 불러온거라서 따로 빼놧음
from django.http import HttpResponse, HttpResponseForbidden

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)  # 저장전에 시간벌자~
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments' : comments,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)


# 현업에서 서버 운영하려면, 각 오류별로 설명을 해줘야 사용자가 당황하지않음
# 디버깅할 떄도 필요하지!! 한가지만 가지고 예시로 진행!
# MDN HTTP에서 오류코드 알 수 있음!
# https://developer.mozilla.org/ko/docs/Web/HTTP/Status
# @require_POST
# def delete(request, pk):
#     article = Article.objects.get(pk=pk)
#     if request.user.is_authenticated:  # 너는 인증 X
#         if request.user == article.user:  # 너는 인증O -> 권한 X
#             article.delete()
#             return redirect('articles:index')
#         return HttpResponseForbidden()  # 403
#     return HttpResponse(status=401)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            # form = ArticleForm(data=request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)


@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)  # commit=False 저장 안하고 저장할거는 return해줌, 타이밍을 만들어주기 위해
            comment.article = article
            comment.user = request.user
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')


# 1번 방법
# 이 방법은 url 일관성 떄문에 2번 방법을 추천!
# def comments_delete(request, comment_pk):
#     comment = Comment.objects.get(pk=comment_pk)
#     article_pk = comment.article.pk
#     comment.delete()
#     return redirect('articles:detail', article_pk)

# 2번방법
@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)

# 댓글 수정은 여기서는 구현하지 않음, 댓글페이지로 이동해야만 가능하기 때문에 패스
# 대신 자바스크립트를 이용해서 할 수 있기 때문에, 이후에 가능