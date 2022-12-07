python manage.py dumpdata --indent 4 accounts.user > users.json <- 앱이름.모델 > 만들 파일명, --indent 4 하면 구조파악하기 쉬움
python manage.py loaddata articles.json comments.json users.json
한꺼번에 이렇게 로드하면되지만, 하나씩 할 때는 관계를 잘 보면서 순서대로 넣어야함. 특히 foreign key여부