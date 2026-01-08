from django import forms
from .models import PPDBRegistration

class PPDBForm(forms.ModelForm):
    class Meta:
        model = PPDBRegistration
        fields = ['full_name', 'gender', 'birth_place', 'birth_date', 
                  'parent_name', 'phone_number', 'address', 'booking_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'booking_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'address': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            # Tambahkan class 'form-control' ke field text lainnya biar rapi ala Bootstrap
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_place': forms.TextInput(attrs={'class': 'form-control'}),
            'parent_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }