from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10)
    # charfield의 경우 글자수의 정의가 필수. text의 경우는 아님.
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번글 - {self.title}: {self.content}'