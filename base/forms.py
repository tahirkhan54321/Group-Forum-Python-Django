# Model based forms for creating forms

from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        # fields will take all of the fields in the Room model and create a form for each
        fields = '__all__'
        exclude = ['host', 'participants']