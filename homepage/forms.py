from django import forms

GRADE_CHOICES = [
    ("", "選択してください"),
    ("小学1年生", "小学1年生"),
    ("小学2年生", "小学2年生"),
    ("小学3年生", "小学3年生"),
    ("小学4年生", "小学4年生"),
    ("小学5年生", "小学5年生"),
    ("小学6年生", "小学6年生"),
    ("中学1年生", "中学1年生"),
    ("中学2年生", "中学2年生"),
    ("中学3年生", "中学3年生"),
    ("高校1年生", "高校1年生"),
    ("高校2年生", "高校2年生"),
    ("高校3年生", "高校3年生"),
]

INQUIRY_CHOICES = [
    ("", "選択してください"),
    ("資料請求", "資料請求"),
    ("無料体験授業", "無料体験授業"),
    ("その他", "その他"),
]

class ContactForm(forms.Form):
    name = forms.CharField(label="お子様のお名前", max_length=50, required=True)
    furigana = forms.CharField(label="お子様のふりがな", max_length=50, required=True)
    grade = forms.ChoiceField(label="お子様の学年", choices=GRADE_CHOICES, required=True)
    tel = forms.CharField(label="お電話番号", max_length=20, required=True)
    email = forms.EmailField(label="Eメールアドレス", required=True)
    zip_code = forms.CharField(label="郵便番号", max_length=10, required=True)
    address = forms.CharField(label="ご住所", max_length=200, required=True)
    building = forms.CharField(label="番地・アパート名・部屋番号", max_length=200, required=True)
    inquiry = forms.ChoiceField(label="お問い合わせ内容", choices=INQUIRY_CHOICES, required=True)
    message = forms.CharField(
        label="その他ご質問・お問い合わせ内容（任意）",
        required=False,
        widget=forms.Textarea(attrs={"rows": 5})
    )
