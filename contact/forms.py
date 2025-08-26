# contact/forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        # モデルのフィールドから、フォームに表示したいものを指定
        fields = [
            'name', 'furigana', 'grade', 'tel', 'email', 'zip_code',
            'address', 'building', 'inquiry', 'message'
        ]
        # Textareaウィジェットの設定もここで可能
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }