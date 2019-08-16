from django.db import models
# Create your models here.
#2.​
class Article(models.Model):
    title = models.CharField(max_length=20) #필수 인자 max_length=숫자
    content = models.TextField()    #필수 인자 없음
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
​
    def __str__(self):
        return f'{self.id}번 글 - {self.title}: {self.content}'
#3. python manage.py makemigrations
#4. python manage.py migrate