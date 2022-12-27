# 코딩 컨벤션 정리해보기

# python
## [PEP8](https://peps.python.org/pep-0008/)

### PDD/final-pjt-back/community/views.py
- 적용전
```python
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import JsonResponse
from .serializers import ReviewListSerializer, ReviewSerializer, CommentSerializer
from .models import Review, Comment
```
- 적용 후
```python
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Review, Comment
from .serializers import ReviewListSerializer, ReviewSerializer, CommentSerializer
```
### PDD/final-pjt-back/accounts/serializers.py
- 적용 전
```python
class UserProfileSerializer(serializers.ModelSerializer):
    like_rating = RatingSerializer(many=True, read_only=True)
    like_reviews = ReviewSerializer(many=True, read_only=True)
    review = ReviewSerializer(many=True, read_only=True)
    like_comments = CommentSerializer(many=True, read_only=True)
    rating = RatingSerializer(many=True, read_only=True)
    community_comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'username', 'profile_image', 'last_login', 'date_joined', 'followings', 'like_rating', 'like_reviews', 'like_comments', 'rating', 'review', 'community_comment')
        read_only_fields = ('followings',)

```
- 적용 후
```python
class UserProfileSerializer(serializers.ModelSerializer):
    like_rating = RatingSerializer(many=True, read_only=True)
    like_reviews = ReviewSerializer(many=True, read_only=True)
    review = ReviewSerializer(many=True, read_only=True)
    like_comments = CommentSerializer(many=True, read_only=True)
    rating = RatingSerializer(many=True, read_only=True)
    community_comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = (
            'id', 'email', 'username',
            'profile_image', 'last_login',
            'date_joined', 'followings',
            'like_rating', 'like_reviews',
            'like_comments', 'rating',
            'review', 'community_comment'
            )
        read_only_fields = ('followings',)

```
# javascript
## [구글](https://google.github.io/styleguide/jsguide.html)
## [카카오](https://tech.kakao.com/2019/12/05/make-better-use-of-eslint/)
- ESLint
  - ESLint = ES + Lint (EcmaScript, 표준javascript + Lint, 에러가 있는 코드에 표시를 달아 놓는 것)
  - 자바스크립트 문법에서 에러를 표시해주는 도구

# java
## [오라클](https://www.oracle.com/java/technologies/javase/codeconventions-comments.html)
## [구글](https://google.github.io/styleguide/javaguide.html)
