from django.contrib import admin
from circulatory_app.models import UserProfile, QuizQuestion, QuizScore, DiseaseInfo

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user__username', 'bio')

@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'correct_answer')
    search_fields = ('question_text',)

@admin.register(QuizScore)
class QuizScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'total_questions', 'date_attempted')
    list_filter = ('date_attempted', 'score')
    search_fields = ('user__username',)

@admin.register(DiseaseInfo)
class DiseaseInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'cause')
    search_fields = ('name',)
