from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Room, Messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse



def community(request):
    rooms = Room.objects.all()
    if request.method == 'POST' and 'move_room' in request.POST:
        room_id = request.POST['room_id']
        if room_id == 'Choose Room':
            return redirect('community')
        else:
            room = Room.objects.filter(pk = room_id)
            if room.exists():
                return redirect('room', room_name = Room.objects.get(pk = room_id).name)
            else:
                return redirect('community')
    context = {
        'title': 'nook | Community',
        'rooms': rooms
    }
    return render(request, 'community/community.html', context)


@login_required
def chatroom(request, room_name):
    if Room.objects.filter(name = room_name).exists():
        room = Room.objects.get(name = room_name)
        context = {
            'title': 'nook | Room',
            'room': room
        }
        return render(request, 'community/chatroom.html', context)
    else:
        return redirect('community')


def sendMessage(request, room_name):
    print('-------------------')
    message = request.POST['messa']
    room_id = request.POST['room_id']
    room = Room.objects.get(pk = room_id)
    user = User.objects.get(username = request.user.username)
    create_message = Messages.objects.create(
        message = message,
        room = room,
        user = user,
        hide_id = 'nohide'
    )
    create_message.save()
    return HttpResponse('Message sent successflly')


def getMessages(request, room_name, room_name1):
    room = Room.objects.get(name = room_name)
    hide_id = 'hide' + str(request.user.pk)
    messages = Messages.objects.filter(room = room)
    # message = []
    # for mess in messages:
    #     if mess.hide_id == hide_id and mess.user == request.user.pk:
    #         pass
    #     else:
    #         message.append(mess)
    # print('-------------------')
    # print(messages)
    return JsonResponse({'messages': list(messages.values())})


def clearchat(request, room_name):
    room = Room.objects.get(name = room_name)
    message = Messages.objects.filter(room = room)
    for mess in message:
        mess.hide = True
        mess.hide_id = 'hide' + str(request.user.pk)
        mess.save()
    return redirect('room', room_name = room_name)



