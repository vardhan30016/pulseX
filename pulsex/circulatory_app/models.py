from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class QuizQuestion(models.Model):
    ANSWER_CHOICES = [
        ('A', 'Option A'),
        ('B', 'Option B'),
        ('C', 'Option C'),
        ('D', 'Option D'),
    ]
    question_text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=1, choices=ANSWER_CHOICES)

    def __str__(self):
        return self.question_text[:50]

class QuizScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_scores')
    score = models.IntegerField()
    total_questions = models.IntegerField()
    date_attempted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.score}/{self.total_questions} on {self.date_attempted.strftime('%Y-%m-%d')}"

class DiseaseInfo(models.Model):
    name = models.CharField(max_length=100)
    cause = models.TextField()
    symptoms = models.TextField()
    prevention = models.TextField()
    image = models.ImageField(upload_to='disease_images/', blank=True, null=True)

    def __str__(self):
        return self.name

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if not hasattr(instance, 'profile'):
        UserProfile.objects.get_or_create(user=instance)
    instance.profile.save()

