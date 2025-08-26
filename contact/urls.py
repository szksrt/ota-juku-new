from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    # お問い合わせフォームページ
    path('', views.ContactView.as_view(), name='index'),
    # 送信完了ページ
    path('success/', views.ContactSuccessView.as_view(), name='success'),
]