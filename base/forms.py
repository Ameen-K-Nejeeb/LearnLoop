from django.forms import ModelForm      
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        db_table = ''
        model = Room
        fields = '__all__'