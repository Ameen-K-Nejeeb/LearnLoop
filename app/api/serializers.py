from rest_framework.serializers import ModelSerializer
from app . models import Room
 

class RoomSerialozer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'