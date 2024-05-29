from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Room

from .serializers import RoomSerialozer


@api_view(["GET"])
def getRoutes(request):
    routes = [
        "GET / api",
        "GET / api/rooms",
        "GET / api/rooms/:id",
    ]
    return Response(routes)


@api_view(["GET"])
def getRooms(requset):
    rooms = Room.objects.all()
    serializer = RoomSerialozer(rooms, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getRoom(requset,pk):
    room = Room.objects.get(id = pk)
    serializer = RoomSerialozer(room, many=False)
    return Response(serializer.data)
