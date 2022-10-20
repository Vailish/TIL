from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)  # 유효성 검사에서 빼서 읽기전용필드로 만들기


class ArticleSerializer(serializers.ModelSerializer):
    # N을 참조하면(비어있더라도) many=True, 검사에서 뺴야하니까 read_only=True
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # 댓글의 pk만 보이는게 아쉽다면 commentserializer 자체를 가지고 만들면됨
    comment_set = CommentSerializer(many=True, read_only=True)  # read_only=True를 쓸 때는 물리적으로 테이블이 존재 할 때만 Meta 아래에 쓰는거 아니면 인자로 넣어야됨
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)  # 'article.comment_set.count() 에서 필요없는거 제거

    class Meta:
        model = Article
        fields = '__all__'

