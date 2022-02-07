from django.forms import ModelForm, TextInput
from .models import Member


class memberForm(ModelForm):
    class Meta:
        model = Member
        fields = ["first_name", "last_name", "father_name", "Age", "email", "mobile", "perma_street", "perma_city", "perma_state", "perma_pin", "pres_street", "pres_city", "pres_state", "pres_pin", "education", "profession", "religion", "varna","signature"]