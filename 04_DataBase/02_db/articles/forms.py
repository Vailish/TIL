from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        # fields = '__all__'
        # 이제는 누가 썻는지 user_id란이 생겼기 때문에
        # 이렇게 하면안됨.(이렇게 하면 글쓴 유저를 선택할수 있게됨)
        # 제외시키던가 골라 넣던가!
        exclude = ('user',)  


class CommentForm(forms.ModelForm):

    class Meta:  # commentForm에대한 정보를 작성하는 클래스
        model = Comment
        # fields = '__all__'
        # 이거의 문제점은 게시글을 선택할 수 있게 됨, 댓글에 작성에 필수 요소이기 떄문에
        # url에서 pk를 받아와서 쓰면 요소 채울 수 있음
        exclude = ('article', 'user',)
