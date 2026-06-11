from django.urls import path
from django.contrib.auth import views as auth_views
from circulatory_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('learn/', views.learn, name='learn'),
    path('simulation/', views.simulation, name='simulation'),
    path('blood/', views.blood, name='blood'),
    path('diseases/', views.diseases, name='diseases'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiz/save-score/', views.save_quiz_score, name='save_quiz_score'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('certificate/', views.certificate, name='certificate'),
]

