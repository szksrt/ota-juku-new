from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm
from contact.models import Contact
from blog.models import Post


class IndexView(generic.TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Postを公開日が新しい順に3件取得して、コンテキストに追加
        context['latest_posts'] = Post.objects.order_by('-published_date')[:3]
        return context

class FeatureView(generic.TemplateView):
    template_name = "feature.html"

class GreetingView(generic.TemplateView):
    template_name = "greeting.html"

class CoursesView(generic.TemplateView):
    template_name = "courses.html"

class CoursesElementaryView(generic.TemplateView):
    template_name = "courses_elementary.html"

class CoursesJuniorView(generic.TemplateView):
    template_name = "courses_junior.html"

class CoursesHighView(generic.TemplateView):
    template_name = "courses_high.html"

class OnlineView(generic.TemplateView):
    template_name = "online.html"

class AdmissionView(generic.TemplateView):
    template_name = "admission.html"

class TrialView(generic.TemplateView):
    template_name = "trial.html"

class FaqView(generic.TemplateView):
    template_name = "faq.html"

class AboutView(generic.TemplateView):
    template_name = "about.html"


class ContactView(generic.FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('homepage:contact')  # URLパターン名に合わせて修正（例: path('contact/', ContactView.as_view(), name='contact')）

    def form_valid(self, form):
        # データベース保存
        Contact.objects.create(
            name=form.cleaned_data['name'],
            furigana=form.cleaned_data['furigana'],
            grade=form.cleaned_data['grade'],
            tel=form.cleaned_data['tel'],
            email=form.cleaned_data['email'],
            zip_code=form.cleaned_data['zip_code'],
            address=form.cleaned_data['address'],
            building=form.cleaned_data['building'],
            inquiry=form.cleaned_data['inquiry'],
            message=form.cleaned_data['message'],
        )

        # メール送信
        subject = f"【太田塾】お問い合わせ（{form.cleaned_data['name']}）"
        message = (
            f"【お子様のお名前】{form.cleaned_data['name']}\n"
            f"【ふりがな】{form.cleaned_data['furigana']}\n"
            f"【学年】{form.cleaned_data['grade']}\n"
            f"【電話番号】{form.cleaned_data['tel']}\n"
            f"【メールアドレス】{form.cleaned_data['email']}\n"
            f"【郵便番号】{form.cleaned_data['zip_code']}\n"
            f"【住所】{form.cleaned_data['address']}\n"
            f"【建物・部屋番号】{form.cleaned_data['building']}\n"
            f"【お問い合わせ内容】{form.cleaned_data['inquiry']}\n"
            f"【その他ご質問・お問い合わせ内容】\n{form.cleaned_data['message']}\n"
        )
        send_mail(
            subject,
            message,
            form.cleaned_data['email'],  # 差出人（ユーザー）
            ['admin@example.com'],        # 宛先（管理者アドレス）
            fail_silently=False,          # エラー時に例外を投げる
        )

        # メッセージ
        messages.success(self.request, "お問い合わせありがとうございます。送信完了しました。")
        return super().form_valid(form)