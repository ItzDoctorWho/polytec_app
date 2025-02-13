from django import forms 
from .models import Member 
class MemberForm(forms.ModelForm): 
    class Meta: 
        model = Member 
        fields = ("full_name", "email", "title", "bio", "city", "github", "twitter", "linkedin", "facebook", "instagram", "website", "picture")