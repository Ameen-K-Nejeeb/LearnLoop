from django.shortcuts import render
from . models import Room
# Create your views here.


#rooms=[
#    {'id':1, 'name':'lets start learn python'},
#    {'id':2, 'name':'start learn django'},
#    {'id':3, 'name':'How far can you go'},
#    {'id':4, 'name':'you are the 5 people you hang around'},
#    {'id':5, 'name':'Lets get started'},
#    {'id':6, 'name':'Have a good journey'},
#]


def home(request,):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'base/home.html',context )

def room(request,pk):
    room = Room.objects.get(id=pk)
#    room = None
#    for i in rooms:
#        if i['id'] == int(pk):
#            room = i
    context = {'room':room}

    return render(request,'base/room.html',context)

