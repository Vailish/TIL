from django.db import models
from django.conf import settings

# 스키마
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      # 장고 내부 순서 때문에 이렇게 나눠서 함
      # settings.AUTH_USER_MODEL 얘는 그냥 User랑 같음 <- models.py에서만 이걸로 씀, 아직 객체가 없기 때문, 문자열반환
      # get_user_model()  <- 나머지는 전부
      # 이렇게 하고 makemigration 하면, 공란을 때문에 물어보는데, 그 이유는 기존에 만들어진 게시물 누가 쓴걸로 할거냐(공란채워라)떄문에 뜸
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # 장고가 알아서 위치가 어디에있든 필드의 마지막에 저장함
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

# article = models.ForeignKey(Article, on_delete=models.CASCADE)
# db에 저장할 때 _id가 붙기 떄문에 생각해서 해주면 됨, 여기서는 article_id
# to, on_delete, **options
# to : 어디에
# on_delete : 부모 게시글이 삭제될 때, 댓글들 어떻게 할거냐
#      - CASCADE : 같이 지우기
#      - PROTECT : 댓글 있으면 못지우게
#      - SET_NULL
#      - SET_DEFAULT
# option 중 # related_name='comments' <- 이 경우에는 comment_set을 전부 comments로 대체

# 쿼리문 미리보기, 위 모델이 OEM을 통해서 SQL로 바뀌면 아래처럼 됨
# $ python manage.py sqlmigrate articles 0002  <- 명령어
#>>>
# BEGIN;
# --
# -- Create model Comment
# --
# CREATE TABLE "articles_comment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content" text NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "article_id" bigint NOT NULL REFERENCES "articles_article" ("id") DEFERRABLE INITIALLY DEFERRED);
# CREATE INDE

# 쉘플러스
# $ python manage.py shell_plus

# dir(article) 이런식으로 쓰면 article 클래스 객체가 사용할 수 있는 메서드 보여줌
