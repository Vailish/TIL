from django import forms  # 관행적으로 forms.py에 form을 모아서 저장함
from .models import Article

# django widget radioselect 이런식으로 검색해보면됨(공식문서에도 잘 되어있음)
# django form field와 widget을 검색해서 해보자!

# class ArticleForm(forms.Form):  # 모델과 관련없고, 모델과 맞춰서 만든것 뿐 / ModelForm은 모델과 밀접한 관련잇음
#     NATION_A = 'kr'  # 이렇게 변수 할당해서 한 번 더쓰는 이유는  django style guide 권장사항임!
#     NATION_B = 'ch'
#     NATION_C = 'jp'
#     NATIONS_CHOICES = [
#         (NATION_A, '한국'),
#         (NATION_B, '중국'),
#         (NATION_C, '일본'),
#     ]
#     # 사용자로부터 멀 받을거냐
#     title = forms.CharField(max_length=10)  # forms에서는 max_length가 필수 요소는 아님
#     content = forms.CharField(widget=forms.Textarea)  # widget은 단순히 출력(렌더링)만 변경해줌, 기능은 form에서 다해줌(ex)유효성검사 등)
#     nation = forms.ChoiceField(choices=NATIONS_CHOICES)

    # nation = forms.ChoiceField(choices=NATIONS_CHOICES, widget=forms.RadioSelect)
    # widget꺼주면 dropbar로 볼 수 있음

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목', 
        widget=forms.TextInput(
            attrs={
                'class': 'my-title form-control',
                'placeholder': 'Enter the title',
                'maxlength': 10,  # 유효성 검사랑 연관(DB저장과) X, django랑 상관없음 widget이니까, tag선에서 막는거임
            }
        )
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content form-control',
                'placeholder': 'Enter the content',
                'row': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': '내용 입력하라고...'
        }
    )

# Meta = data를 표현하기 위한 data
# ModelForm이 class Meta를 쓰게끔 설계되어있는것, 문법적 요소로 생각하지말자, framework를 쓰는 이유를 생각하자
    class Meta:  # 설정 변경하면 안됨, 그대로만
        model = Article  # 어떤 모델을 기반으로 할지, 호출하는게 아님 Article()이 아님(인스턴스생성이 아닌 그 자체를 쓰는것)
        # fields = ('title', 'content', )  # 필요하다면 이런식으로 (Model에서 받아오는 부분)명시할 수 있음, 튜플이나 리스트로
        fields = '__all__'  # 어떤 모델필드 중 어떤것을 출력할지/ __all__ 사용자에게 입력받은 모든 값
        # exclude = ('title', )  # 이러면 title은 빠짐, fields 사용안하고 얘만 써도 되는 듯?

# 참조값과 반환값 함수와 클래스와 비슷함

# def greeting():
#     return '안녕하세요'

# print(greeting)  # <function greeting at 0x~> 참조값을 그대로 넘김 ex) views.index
# print(greeting())  # 안녕하세요

# 참조값을 왜 쓰냐 필요할때 호출하겠다 임

'''
ModelForm 과 Form보다 더 좋은 것이 아닌 역할이 다른 것이다.
Form - 사용자로부터 받는 데이터가 DB와 연관되어 있지 않는 경우에 사용
     - DB에 영향을 미치지 않고 단순 데이터만 사용되는 경우
        - ex) 로그인 : 인증 과정에서만 사용 후 별도에 DB에 저장하지 않음
ModelForm - 사용자로부터 받는 데이터가 DB와 연관되어있는 경우에 사용
          - 데이터의 유효성 검사가 끝나면 데이터를 각각 어떤 레코드에 맵핑해야 할 지 이미 갖고 있기 때문에 곧바로 save() 호출이 가능
'''

# django-bootstrap-v5 검색해서 깔아서 부트스트랩처럼 써도됨
# 설치 후엔 잘 찾아보기, app에 등록을 하던가, requirements를 업데이트하던가 등등 있음