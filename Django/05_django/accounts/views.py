from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm # UserCreationForm <- CustomUserCreationForm을 만들었기 떄문
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Create your views here.
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:  # 주소를 입력해도 되돌려보냄
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, date=request.POST) 위와 똑같음
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')  # 단축평가 앞에가 있다면 or이니까 그냥 뒤에꺼는 안감, 이걸 해주는 이유는 login_required를 걸어줬을 때, next 주소로 넘겨주기 위해서 처리해주는 거고, if문 써서 해도됨
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    # 로그아웃
    auth_logout(request)
    return redirect('articles:index')

# create
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # 회원가입에서 저장을 한다? 유저 만들기, save를 공식문서나 깃허브에 들어가서 보면 user를 return해줌을 알 수 있음
            # 회원가입 후 로그인
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()  # ModelForm이므로 이안에 auth_user가 아닌 user가 들어있음 -> 오버라이드 해주면됨
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def delete(request):
    request.user.delete()
    auth_logout(request.user)  # 안해도 만료되서 알아서 되겠지만, 로그아웃 해주면 되는데
    # 순서는 로그아웃이 뒤에, 그 이유는 로그아웃을 해버리면 탈퇴할 유저 정보가 날라가기 때문에
    return redirect('articles:index')

@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method =='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # 혹은 user = form.save() 해서 써줘도 됨, 이걸로 인해 로그아웃 안됨
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)  # 다른 class와 다르게 필수 위치인자로 request.user를 받음 <- 상위인 SetPasswordForm에서 받아서 그렇게 됨
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)