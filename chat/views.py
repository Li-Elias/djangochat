from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    
    return render(request, 'room.html', {
        'room_name': room,
        'username': username,
        })

def home_submit(request):
    room_name = request.POST['room_name']
    username = request.POST['username']
    
    if Room.objects.filter(name=room_name).exists():
        return redirect('/'+room_name+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room_name)
        new_room.save()
        return redirect('/'+room_name+'/?username='+username)
    
def message(request):
    message = request.POST['message']
    username = request.POST['username']
    room_name = request.POST['room_name']
    room = Room.objects.get(name=room_name)
    
    new_message = Message.objects.create(message=message, user=username, room=room)
    new_message.save()
    return HttpResponse('Message sent successfully')

def get_messages(request, room):
    room = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room)
    
    return JsonResponse({"messages":list(messages.values())})
