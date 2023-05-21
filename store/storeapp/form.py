from django import forms

from storeapp.models import Department,Course,Materials


class orderCreationForm(forms.ModelForm):
    class Meta:
        model = Materials
        fields = ('department','course')

def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()
