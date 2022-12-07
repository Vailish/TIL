import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')  # 무조건 request 첫번째, 두번째는 어디로, 세번째부터? 데이터


def greeting(request):
    today = datetime.datetime(2022, 8, 8, 10, 2)
    context = {
        'name': 'justin',
        'foods': ['apple', 'chicken', 'burger'],
        'today' : today
    }
    return render(request, 'articles/greeting.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    # print(request)
    # print(type(request))
    # print(request.GET.get('message'))
    department = request.GET.get('department')
    name = request.GET.get('name')

    if department == '대전 2반':
        if name == '김영주':
            message = '교수님이시군요!'
        else:
            message = '교육생이시군요!'
    else:
        message = '다른 반이시군요!'

    context = {
        'message':message,        
    }
    return render(request, 'articles/catch.html', context)

def show(request, name):
    context = {
        'name':name
    }
    return  render(request, 'articles/show.html', context)