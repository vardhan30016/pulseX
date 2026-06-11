from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from circulatory_app.forms import RegisterForm, UserProfileForm
from circulatory_app.models import QuizScore, QuizQuestion, DiseaseInfo, UserProfile
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def home(request):
    return render(request, 'index.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def learn(request):
    return render(request, 'learn.html')

def simulation(request):
    return render(request, 'simulation.html')

def blood(request):
    return render(request, 'blood.html')

def diseases(request):
    if DiseaseInfo.objects.count() == 0:
        diseases_data = [
            {
                "name": "Heart Attack (Myocardial Infarction)",
                "cause": "Occurs when blood flow to a part of the heart muscle is severely reduced or blocked, usually due to a buildup of fat, cholesterol, and other substances forming a plaque in the coronary arteries.",
                "symptoms": "Chest pain or pressure (angina), shortness of breath, radiating pain in the left arm, neck, jaw or back, cold sweats, and lightheadedness.",
                "prevention": "Maintain a heart-healthy diet, exercise regularly, manage stress, avoid smoking, and monitor blood pressure and cholesterol levels."
            },
            {
                "name": "Hypertension (High Blood Pressure)",
                "cause": "A chronic condition where the force of the blood pushing against the artery walls is consistently too high. Caused by genetics, high salt diet, physical inactivity, obesity, and chronic stress.",
                "symptoms": "Often referred to as a \"silent killer\" because it has no obvious warning signs. Severe cases may cause headaches, nosebleeds, fatigue, or chest pain.",
                "prevention": "Reduce sodium intake, increase potassium consumption, limit alcohol, engage in regular cardiovascular activity, and maintain a healthy weight."
            },
            {
                "name": "Stroke (Cerebrovascular Accident)",
                "cause": "Triggered when blood supply to a part of the brain is interrupted or reduced (ischemic), or when a blood vessel in the brain bursts (hemorrhagic), depriving brain tissue of oxygen.",
                "symptoms": "Sudden numbness or weakness in the face, arm, or leg (especially on one side), confusion, trouble speaking, difficulty seeing, loss of balance, and severe headache.",
                "prevention": "Control high blood pressure, manage diabetes, maintain cholesterol in a healthy range, treat atrial fibrillation, and eat a low-sodium, low-fat diet."
            },
            {
                "name": "Anemia",
                "cause": "A condition characterized by a lack of healthy red blood cells or hemoglobin to carry sufficient oxygen to body tissues. Primarily caused by iron deficiency, vitamin deficiencies, chronic diseases, or blood loss.",
                "symptoms": "Persistent fatigue, generalized weakness, pale or yellowish skin, cold hands and feet, dizziness, irregular heartbeats, and chest pain.",
                "prevention": "Eat a diet rich in iron (spinach, red meat, beans), vitamin B12, and folate. Pair iron-rich foods with Vitamin C to increase iron absorption."
            }
        ]
        for d in diseases_data:
            DiseaseInfo.objects.create(**d)
            
    diseases = DiseaseInfo.objects.all()
    return render(request, 'diseases.html', {'diseases': diseases})

def quiz(request):
    if QuizQuestion.objects.count() == 0:
        questions_data = [
            {
                "question_text": "Which chamber of the heart pumps oxygenated blood to the rest of the body?",
                "option_a": "Right Atrium",
                "option_b": "Right Ventricle",
                "option_c": "Left Atrium",
                "option_d": "Left Ventricle",
                "correct_answer": "D"
            },
            {
                "question_text": "What type of blood vessel carries blood away from the heart?",
                "option_a": "Arteries",
                "option_b": "Veins",
                "option_c": "Capillaries",
                "option_d": "Lymphatics",
                "correct_answer": "A"
            },
            {
                "question_text": "What is the primary function of Red Blood Cells?",
                "option_a": "Fights infection and foreign invaders",
                "option_b": "Facilitates blood coagulation",
                "option_c": "Transports oxygen using hemoglobin",
                "option_d": "Distributes nutrients in liquid matrix",
                "correct_answer": "C"
            },
            {
                "question_text": "Which protein in red blood cells binds to oxygen?",
                "option_a": "Fibrinogen",
                "option_b": "Hemoglobin",
                "option_c": "Myoglobin",
                "option_d": "Albumin",
                "correct_answer": "B"
            },
            {
                "question_text": "What is the normal resting blood pressure range for an adult?",
                "option_a": "140/90 mmHg",
                "option_b": "90/60 mmHg",
                "option_c": "120/80 mmHg",
                "option_d": "160/100 mmHg",
                "correct_answer": "C"
            },
            {
                "question_text": "Which component of blood is responsible for blood clotting?",
                "option_a": "White Blood Cells",
                "option_b": "Plasma",
                "option_c": "Platelets",
                "option_d": "Lymphocytes",
                "correct_answer": "C"
            },
            {
                "question_text": "What circulatory condition is characterized by chronically high blood pressure?",
                "option_a": "Hypertension",
                "option_b": "Anemia",
                "option_c": "Stroke",
                "option_d": "Heart Attack",
                "correct_answer": "A"
            },
            {
                "question_text": "Which heart valve separates the left atrium from the left ventricle?",
                "option_a": "Tricuspid Valve",
                "option_b": "Mitral (Bicuspid) Valve",
                "option_c": "Pulmonary Valve",
                "option_d": "Aortic Valve",
                "correct_answer": "B"
            },
            {
                "question_text": "How many chambers does the human heart have?",
                "option_a": "Two",
                "option_b": "Three",
                "option_c": "Four",
                "option_d": "Five",
                "correct_answer": "C"
            },
            {
                "question_text": "What component makes up the largest percentage of human blood volume?",
                "option_a": "Red Blood Cells",
                "option_b": "White Blood Cells",
                "option_c": "Platelets",
                "option_d": "Plasma",
                "correct_answer": "D"
            }
        ]
        for q in questions_data:
            QuizQuestion.objects.create(**q)
            
    questions = QuizQuestion.objects.all()
    return render(request, 'quiz.html', {'questions': questions})

@require_POST
def save_quiz_score(request):
    if request.user.is_authenticated:
        try:
            data = json.loads(request.body)
            score = int(data.get('score'))
            total_questions = int(data.get('total_questions'))
            
            quiz_score = QuizScore.objects.create(
                user=request.user,
                score=score,
                total_questions=total_questions
            )
            return JsonResponse({"status": "success", "score_id": quiz_score.id})
        except (ValueError, TypeError, json.JSONDecodeError):
            return JsonResponse({"status": "error", "message": "Invalid data format."}, status=400)
    else:
        return JsonResponse({"status": "guest", "message": "Scores are not saved for guest users."})

@login_required
def dashboard(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=profile)

    scores = QuizScore.objects.filter(user=request.user).order_by('-date_attempted')
    return render(request, 'dashboard.html', {'scores': scores, 'profile_form': form, 'profile': profile})


@login_required
def certificate(request):
    return render(request, 'certificate.html')


