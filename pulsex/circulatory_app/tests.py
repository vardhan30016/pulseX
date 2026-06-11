from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from circulatory_app.models import DiseaseInfo, QuizQuestion, QuizScore

class CirculatoryAppTests(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_learn_page(self):
        response = self.client.get(reverse('learn'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learn.html')

    def test_diseases_page_seeds_and_loads(self):
        self.assertEqual(DiseaseInfo.objects.count(), 0)
        response = self.client.get(reverse('diseases'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'diseases.html')
        self.assertGreater(DiseaseInfo.objects.count(), 0)

    def test_quiz_page_seeds_and_loads(self):
        self.assertEqual(QuizQuestion.objects.count(), 0)
        response = self.client.get(reverse('quiz'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quiz.html')
        self.assertGreater(QuizQuestion.objects.count(), 0)

    def test_dashboard_redirects_unauthenticated(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)

    def test_dashboard_loads_authenticated(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')

