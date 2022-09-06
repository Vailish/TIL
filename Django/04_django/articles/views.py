from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Article
from .forms import ArticleForm


# 데코레이터가 먼저 실행됨, GET인 요청에만 아래 함수를 쓸 수 있게함. 아니면 405 응답번호를 줌(4-> 클라이언트 잘못)
@require_safe
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)

# new와 create는 method만 다르고 같음, 둘만 분기로 나눠주면 하나로 합칠 수 있음!
@require_http_methods(['GET', 'POST'])  # 리스트 안만 받아주고 나머지는 쳐짐
def create(request):
    if request.method == 'POST':  # 왜 하필 POST를 먼저보냐, else일때 생각해보면됨, DB조작관련은 얘만 하기때문에 중요
        # create
        form = ArticleForm(request.POST)  # modelform에서 알아서 맵핑해줌
        if form.is_valid():  # 검증과정
            article = form.save()  # 새 글을 article에 저장
            return redirect('articles:detail', article.pk)
    else:  # GET 말고도 다른 메서드도 있음. 그래서 if =='POST' 이런 식으로 짜는 것!, Decorater가 있어서 GET만 해당, 하지만 지우진 않음, 구조를 꺠는게 이상한 것
        # new
        form = ArticleForm()
    # 이렇게 들여쓰기 하는게 맞음 is_valid를 통과 못하면 갈 곳이 없기 때문에 그래서 new 부분이 하나고 나머지는 공통으로 쓰게됨
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

@require_safe
def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    # if request.method == 'POST':  # 이 조건이 빠지면, url을 통해서 해커들이 회원 탈퇴 시키는 등 마음대로 조작할 수 있게됨;
                                  # POST는 body에 데이터를 보냄, @가 있어서 if가 필요없음\
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form': form,
#     }
#     return render(request, 'articles/edit.html', context)

# update와 edit 합치기
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)  # instance=article : 이게 있으면 수정, 아니면 생성
        # form = ArticleForm(data=request.POST, instance=article)  # 위랑 같은 코드, data는 생략되어있는거, 하지만 instance는 생략불가
        # -> 부모에서 인자 자리가 data가 2번쨰(self 다음)이기 떄문에 생략 가능한 것, 그 다음은 files기 때문에 instance를 생략하면 files로 인식해서 오류나는 것
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)