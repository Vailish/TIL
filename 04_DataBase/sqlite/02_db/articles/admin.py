from django.contrib import admin
from .models import Article, Comment

# Register your models here.
admin.site.register(Article)  # 같이 넣어주면 안됨
admin.site.register(Comment)  # 이렇게 넣어줘야 admin에서 comment 볼 수 있음
