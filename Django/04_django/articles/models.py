from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)  # 유효성검사에 추가, Field도 유효성검사
    content = models.TextField()  # Modelform에서 알아서 바꿔줌 textfield -> textarea
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
