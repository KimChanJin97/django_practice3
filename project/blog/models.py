from django.db import models

# db테이블 하나가 class 하나에 대응

class Blog(models.Model):
    title = models.CharField(max_length=20)
    sub_title = models.CharField(max_length=30, default="")
    content = models.TextField()
    modified_number = models.IntegerField(default=0)
    whoisincharge = models.CharField(max_length=10, default="")
    
    
    created_at = models.DateTimeField(auto_now_add=True)
# model에 변경사항 있으면 터미널에서 migration 해줘야함
# python manage.py makemigrations
# python manage.py migrate

# 이후 생성한 class 를 admin 에 등록해야 함
    def __str__(self):
        return self.title
# 객체 이름을 사용자 입맛에 맞게 커스터마이징하는 코드

# 객체는 한줄
# 콜럼은 title, content, created_at 등 index들
# 값은 직접 admin 페이지에서 만들든가 shell로 만들든가

# Blog.objects.all() -> 클래스 title, content, created_at 키 가져오기
# Blog.objects.get(pk=?) -> 클래스 title, content, created_at 값 가져오기