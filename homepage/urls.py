from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('feature/', views.FeatureView.as_view(), name="feature"),
    path('greeting/', views.GreetingView.as_view(), name="greeting"),
    path('courses/', views.CoursesView.as_view(), name="courses"),
    path('courses/elementary/', views.CoursesElementaryView.as_view(), name="courses_elementary"),
    path('courses/junior/', views.CoursesJuniorView.as_view(), name="courses_junior"),
    path('courses/high/', views.CoursesHighView.as_view(), name="courses_high"),
    path('online/', views.OnlineView.as_view(), name="online"),
    path('admission/', views.AdmissionView.as_view(), name="admission"),
    path('trial/', views.TrialView.as_view(), name="trial"),
    path('faq/', views.FaqView.as_view(), name="faq"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('contact/', views.ContactView.as_view(), name="contact"),
]
