from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from .models import Room
from users.models import UserPreferences as UserPref, User

from riotwatcher import LolWatcher
from decouple import config

def room(request):
  if not request.user.is_authenticated:
    return redirect('home')

  username = request.user.username_lol
  if request.method == 'POST':
    match_id = int(request.POST.get('button_value'))
    my_id = request.user.id
    my_object = User.objects.filter(id=my_id)[0]
    duo_object = User.objects.filter(id=match_id)[0]
    room_id = None

    if my_id > match_id:
      duo_date = str(duo_object.date_joined).split(' ')
      duo_date = duo_date[0].split('-')
      duo_date = duo_date[0] + duo_date[1] + duo_date[2]

      room_id = str(duo_object.id) + str(my_object.id) + duo_date
    else:
      my_date = str(my_object.date_joined).split(' ')
      my_date = my_date[0].split('-')
      my_date = my_date[0] + my_date[1] + my_date[2]
      
      room_id = str(my_object.id) + str(duo_object.id) + my_date

    print(room_id)
    if not Room.objects.filter(name=room_id).exists():
      Room.objects.create(name=room_id)

    messages = Room.objects.filter(name=room_id)[0].messages

    msg_len = len(messages)
    print(msg_len)
    print(messages)

    """ for i in range(0, msg_len):
      if messages[i].content == '':
        print('Deletando mensagem vazia!')
        messages[i].delete()

    if msg_len > 25:
      for i in range(0, msg_len-25):
        messages[i].delete()
      messages = Message.objects.filter(room=room_id)[0:25] """

    duo_username_lol = UserPref.objects.filter(user_id=match_id)[0].user.username_lol

    return JsonResponse({
      'room_name': room_id,
      'username': username,
      'messages': messages,
      'duo_username_lol': duo_username_lol
    })

  # Show matches in the left
  matches_id = UserPref.objects.filter(user_id=request.user.id)[0].match
  matches_id = matches_id.split(',')
  for i in range(0, len(matches_id)):
    matches_id[i] = int(matches_id[i])
  matches_id.remove(0)

  matched_users = UserPref.objects.filter(user_id__in=matches_id)

  # Profile picture
  API_KEY = config('API_KEY')
  watcher = LolWatcher(api_key=API_KEY)
  region = 'br1'

  icon_list = []
  for duo in matched_users:
    summoner_puuid = duo.user.puuid
    account_info = watcher.summoner.by_puuid(region=region, encrypted_puuid=summoner_puuid)
    summoner_icon = account_info['profileIconId']
    icon_list.append(summoner_icon)

  matched_users = zip(matched_users, icon_list)
  game_version = config('GAME_VERSION')

  return render(request, 'chat/room.html', {
    'username': username,
    'matched_users': matched_users,
    'game_version': game_version
  })

def send(request):
  # Put room in the field 'teste'
  if request.method == 'POST':
    room_name = request.POST.get('room_name')
    message = request.POST.get('message')
    username = request.POST.get('username')

    room = Room.objects.filter(name=room_name)
    db_msg = room[0].messages
    if len(db_msg) >= 10:
      extra_msg = len(db_msg) - 10
      del db_msg[0:extra_msg]

    # Receive parameters and put them here (username, message)
    my_msg = {'username': username, 'message': message}
    db_msg.append(my_msg)
    print(db_msg)
    print(len(db_msg))
    save_message = Room.objects.filter(name=room_name).update(messages=db_msg)
    return JsonResponse({
      'username': username,
      'message': message
    })

def get_messages(request):
  username = request.user.username_lol
  room = request.POST.get('room_name')
  room_messages = Room.objects.filter(name=room)[0].messages
  return JsonResponse({
    'messages': room_messages,
    'username': username
  })
