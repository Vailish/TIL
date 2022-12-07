from django.db import models
from django.conf import settings
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField, ImageSpecField

def articles_image_path(instance, filename):  # pk로는 못 받음, 경로가 만들어질때는 pk가 아직 없기 때문에
    return f'images/{instance.user.username}/{filename}'

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(blank=True)  # blank=True : 비어있어도 된다, 이게 없다면 필수요소가됨,
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(200,300)],
        format='JPEG',
        options={'quality': 80},
    )


    # 이미지 필드는Pillow라는 라이브러리 받아야 사용가능
    # image = models.ImageField(blank=True, upload_to='images/')
    # image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    # image = models.ImageField(blank=True, upload_to=articles_image_path)
    # image = ProcessedImageField(
    #     blank=True,
    #     upload_to='thumbnails/',
    #     processors=[Thumbnail(200,300)],
    #     format='JPEG',
    #     options={'quality': 80},
    # )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # blank vs null
    # blank : True인 경우 필드를 비워 둘 수 있음 - 이 경우 DB에는 빈 문자열 저장
    #         유효성 검사에서 사용 됨(is_valid), Validation-related
    # null : True인 경우 빈 값을 DB에 Null로 저장함, Database-related / is_valid에 통과됨(null도 값이니까)
    
    # CharField, TextField와 같은 문자열 기반 필드에는 null 옵션 사용을 피해야함.
    # 문자열에서는 빈 문자열이 존재함으로, 두 가지 경우를 만들 필요는 없음

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
