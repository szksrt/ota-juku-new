# contact/admin.py

from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # 管理サイトの一覧に表示したい項目
    list_display = ('name', 'grade', 'inquiry', 'created_at')
    # 日付で絞り込めるようにする
    list_filter = ('created_at',)
    # 名前で検索できるようにする
    search_fields = ('name', 'furigana')