from django.views import generic
from blog.models import Post

# -----------------------------------------------------------------
# トップページ
# -----------------------------------------------------------------
class IndexView(generic.TemplateView):
    template_name = "homepage/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Postを公開日が新しい順に3件取得して、コンテキストに追加
        context['latest_posts'] = Post.objects.order_by('-published_date')[:3]
        return context

# -----------------------------------------------------------------
# 静的ページ
# -----------------------------------------------------------------
class FeatureView(generic.TemplateView):
    template_name = "homepage/feature.html"

class GreetingView(generic.TemplateView):
    template_name = "homepage/greeting.html"

class CoursesView(generic.TemplateView):
    template_name = "homepage/courses.html"

class CoursesElementaryView(generic.TemplateView):
    template_name = "homepage/courses_elementary.html"

class CoursesJuniorView(generic.TemplateView):
    template_name = "homepage/courses_junior.html"

class CoursesHighView(generic.TemplateView):
    template_name = "homepage/courses_high.html"

class OnlineView(generic.TemplateView):
    template_name = "homepage/online.html"

class AdmissionView(generic.TemplateView):
    template_name = "homepage/admission.html"

class TrialView(generic.TemplateView):
    template_name = "homepage/trial.html"

class FaqView(generic.TemplateView):
    template_name = "homepage/faq.html"

class AboutView(generic.TemplateView):
    template_name = "homepage/about.html"