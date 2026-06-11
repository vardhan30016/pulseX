from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from circulatory_app.models import UserProfile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Provide a valid email address.")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Tell us about your cardiovascular study goals...'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }

