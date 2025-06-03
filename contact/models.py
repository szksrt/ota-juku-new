from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    furigana = models.CharField(max_length=50)
    grade = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    email = models.EmailField()
    zip_code = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    building = models.CharField(max_length=200)
    inquiry = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}（{self.grade}）"
