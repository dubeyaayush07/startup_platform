from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.http import JsonResponse
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import ChatGrant
from .models import Room
from django.contrib.auth.decorators import login_required
 

# Create your views here.

from .models import Room


@login_required
def all_rooms(request):

    if request.user.profile.role == 'M':
        rooms = Room.objects.filter(mentor=request.user.username)
    else:
        rooms = Room.objects.filter(startup=request.user.username)

    return render(request, 'chat/index.html', {'rooms': rooms})

@login_required
def room_detail(request, slug):
    room = Room.objects.get(slug=slug)
    return render(request, 'chat/room_detail.html', {'room': room})
    
@login_required
def add_room(request, username):
    room_name = f'{request.user.username}-{username}'
    if len(Room.objects.filter(name = room_name)) != 0:
        return redirect('all_rooms')
    Room.objects.create(name=room_name, slug=room_name, description="This is a chat", startup=username, mentor=request.user.username)
    return redirect('all_rooms')





def token(request):
    identity = request.GET.get('identity', request.user.username)
    device_id = request.GET.get('device', 'default')  # unique device ID

    account_sid = settings.TWILIO_ACCOUNT_SID
    api_key = settings.TWILIO_API_KEY
    api_secret = settings.TWILIO_API_SECRET
    chat_service_sid = settings.TWILIO_CHAT_SERVICE_SID

    token = AccessToken(account_sid, api_key, api_secret, identity=identity)

    # Create a unique endpoint ID for the device
    endpoint = "MyDjangoChatRoom:{0}:{1}".format(identity, device_id)

    if chat_service_sid:
        chat_grant = ChatGrant(endpoint_id=endpoint,
                               service_sid=chat_service_sid)
        token.add_grant(chat_grant)

    response = {
        'identity': identity,
        'token': token.to_jwt().decode('utf-8')
    }

    return JsonResponse(response)