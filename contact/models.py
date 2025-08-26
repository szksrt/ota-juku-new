# contact/models.py
from django.db import models

class Contact(models.Model):
    GRADE_CHOICES = [
        ("小学1年生", "小学1年生"), ("小学2年生", "小学2年生"), ("小学3年生", "小学3年生"),
        ("小学4年生", "小学4年生"), ("小学5年生", "小学5年生"), ("小学6年生", "小学6年生"),
        ("中学1年生", "中学1年生"), ("中学2年生", "中学2年生"), ("中学3年生", "中学3年生"),
        ("高校1年生", "高校1年生"), ("高校2年生", "高校2年生"), ("高校3年生", "高校3年生"),
    ]
    INQUIRY_CHOICES = [
        ("資料請求", "資料請求"), ("無料体験授業", "無料体験授業"), ("その他", "その他"),
    ]

    name = models.CharField("お子様のお名前", max_length=50)
    furigana = models.CharField("お子様のふりがな", max_length=50)
    grade = models.CharField("お子様の学年", max_length=20, choices=GRADE_CHOICES)
    tel = models.CharField("お電話番号", max_length=20)
    email = models.EmailField("Eメールアドレス")
    zip_code = models.CharField("郵便番号", max_length=10)
    address = models.CharField("ご住所", max_length=200)
    building = models.CharField("番地・アパート名・部屋番号", max_length=200, blank=True)
    inquiry = models.CharField("お問い合わせ内容", max_length=20, choices=INQUIRY_CHOICES)
    message = models.TextField("その他ご質問など（任意）", blank=True)
    created_at = models.DateTimeField("受付日時", auto_now_add=True)

    def __str__(self):
        return f"{self.name}（{self.grade}）"