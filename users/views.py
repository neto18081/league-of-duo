from django import http
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.db.models import Q
from django.http.response import HttpResponse, JsonResponse
from users.models import User, UserPreferences as UserPref
from django.shortcuts import redirect, render
from users.forms import UserCreationForm, UserPreferences
import urllib.request, json

from riotwatcher import LolWatcher
from decouple import config
from random import shuffle

game_version = config('GAME_VERSION')

def riot(request):
  return HttpResponse('<p>d24135b8-d169-4b39-a91d-c9ff74f9898e</p>')

def home(request):
  return render(request, 'home.html')
 
def register(request):
  if request.user.is_authenticated:
    return redirect('/profile')
  if request.method == 'POST':
    form = UserCreationForm(request.POST)

    API_KEY = config('API_KEY')
    watcher = LolWatcher(api_key=API_KEY)
    region = 'br1'
    summoner_username_lol = form['username_lol'].value().lower()
    summoner_username = form['username'].value().lower()
    summoner_email = form['email'].value().lower()
    summoner_password1 = form['password1'].value()
    summoner_password2 = form['password2'].value()

    """ username_lol_exists = User.objects.filter(username_lol__iexact=summoner_username_lol).exists() """
    username_exists = User.objects.filter(username__iexact=summoner_username).exists()
    email_exists = User.objects.filter(email=summoner_email).exists()

    """ if username_lol_exists:
      return render(request, 'register.html', {'form': form, 'error': 'Usuário do lol já cadastrado!' ,'type': 'id_username_lol'}) """
    if username_exists:
      return render(request, 'register.html', {'form': form, 'error': 'Usuário já cadastrado!', 'type': 'id_username'})
    elif email_exists:
      return render(request, 'register.html', {'form': form, 'error': 'Email já cadastrado!','type': 'id_email'})
    elif summoner_password1 != summoner_password2:
      return render(request, 'register.html', {'form': form, 'error': 'As senhas devem ser iguais!','type': 'id_password1'})
    elif len(summoner_password1) < 8:
      return render(request, 'register.html', {'form': form, 'error': 'A senha deve ter pelo menos 8 caracteres.','type': 'id_password1'})
    elif summoner_password1.isdecimal():
      return render(request, 'register.html', {'form': form, 'error': 'A senha deve conter letras!','type': 'id_password1'})
    else:
      # Verifica se o usuário existe no LOL
      try:
        account_info = watcher.summoner.by_name(region=region, summoner_name=summoner_username_lol)
        print('Usuário existente')
      except:
        return render(request, 'register.html', {'form': form, 'error': 'Usuário inválido!', 'type': 'id_username_lol'})
      else:
        if form.is_valid():
          new_user = form.save()
          user = User.objects.filter(username_lol__iexact=summoner_username_lol).update(puuid=account_info['puuid'])

          # Logando o usuário criado
          new_user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
          )
          login(request, new_user)
          return redirect('/preferences')

  else:
    form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def profile(request):
  if request.user.is_authenticated:
    # GET SUMMONER ICON
    # Fetch information for icon Id and for the patch version
    API_KEY = config('API_KEY')
    watcher = LolWatcher(api_key=API_KEY)
    region = 'br1'
    summoner_name = request.user.username_lol

    account_info = watcher.summoner.by_name(region=region, summoner_name=summoner_name)

    rank_info = watcher.league.by_summoner(region=region,encrypted_summoner_id=account_info['id'])

    summoner_icon = account_info['profileIconId']

    profile_icon_url = f'https://ddragon.leagueoflegends.com/cdn/{game_version}/img/profileicon/{summoner_icon}.png'

    summoner_tier = 'Unranked'
    if rank_info != []:
      for i in range(0, len(rank_info)):
        if rank_info[i]['queueType'] == 'RANKED_SOLO_5x5':
          summoner_tier = rank_info[i]['tier']

    # User preferences
    exists_pref = UserPref.objects.filter(user=request.user).exists()

    up = None
    if exists_pref:
      up = UserPref.objects.get(user=request.user)
      print('PREFERENCIA DO USUÁRIO:',up)
    else:
      up = None
      return redirect('/preferences')
    
    return render(request, 'profile.html', {
      'profile_icons_url':profile_icon_url,
      'userpref': up,
      'summoner_tier': summoner_tier
      })
  else:
    return redirect('home')

def cards(request):
  if request.user.is_authenticated:
    # Banco de dados do usuário
    if request.method == 'POST':
      user_db = UserPref.objects.get(user_id=request.user.id)
      user_filter_db = UserPref.objects.filter(user_id=request.user.id)
      # Verifica se o duo foi recusado ou aceito
      cards_response = request.POST.get('duo_status')
      cards_response = cards_response.split(',')
      card_id = cards_response[1]
      my_id = str(request.user.id)

      # Duo match
      possible_match_user = user_filter_db[0].duo_match
      possible_match_user = possible_match_user.split(',')
      new_possible_match = '0'

      if len(possible_match_user) > 1:
        if card_id == possible_match_user[1]:
          if cards_response[0] == 'accept':
            duo_db = UserPref.objects.filter(user_id=card_id)

            match_user = user_filter_db[0].match+','+card_id
            match_duo = duo_db[0].match+','+str(request.user.id)
            save_match_user = user_filter_db.update(match=match_user)
            save_match_duo = duo_db.update(match=match_duo)

      if cards_response[0] == 'refuse':
        duo_refused_column = user_filter_db[0].duo_refused
        already_exists = False
        test_exists = duo_refused_column.split(',')
        for data in test_exists:
          if data == card_id:
            already_exists = True

        if not already_exists:
          new_refused = duo_refused_column+','+card_id
          save_refused = user_filter_db.update(duo_refused=new_refused)
          print('Duo recusado!')

      else:
        duo_accepted_column = user_filter_db[0].duo_accepted
        already_exists = False
        test_exists = duo_accepted_column.split(',')

        for data in test_exists:
          if data == card_id:
            already_exists = True

        if not already_exists:
          # Adicionar no duo match
          user_filter_db = UserPref.objects.filter(user_id=request.user.id)
          my_duo_match = user_filter_db[0].duo_match
          my_duo_match = my_duo_match.split(',')
          already_accepted = False
          print(my_duo_match)

          for duo in my_duo_match:
            if duo == card_id:
              print(duo)
              already_accepted = True
          print('Duo ja consta no meu campo:',already_accepted)

          if not already_accepted:
            duo_match = UserPref.objects.filter(user_id=card_id)[0].duo_match
            match = duo_match+','+my_id
            save_match = UserPref.objects.filter(user_id=card_id).update(duo_match=match)
            print('Adicionado no duo_match do duo!')

          new_accepted = duo_accepted_column+','+card_id
          save_accepted = user_filter_db.update(duo_accepted=new_accepted)
          print('Duo aceito!')

      user_db = UserPref.objects.get(user_id=request.user.id)
      user_filter_db = UserPref.objects.filter(user_id=request.user.id)

      duo_db = UserPref.objects.filter(user_id=card_id)
      match_verify = user_filter_db[0].duo_match
      match_verify = match_verify.split(',')
      match_exists = False

      # Verify if match exists
      for match in match_verify:
        if match == card_id:
          match_exists = True

      print(match_exists)
      duo_match_column = user_filter_db[0].duo_match
      duo_match_column = duo_match_column.split(',')
      new_duo_match = '0'
      if len(duo_match_column) > 1:
        for i in range(2, len(duo_match_column)):
          new_duo_match = new_duo_match+','+duo_match_column[i]

      delete_already_matched = user_filter_db.update(duo_match=new_duo_match)
      duo_position = user_db.duo_position
      duo_position_size = len(duo_position)
      
      duo_position_filter = None
      if duo_position_size == 1:
        duo_position_filter = (
        Q(first_position__icontains=duo_position[0]))
      elif duo_position_size == 2:
        duo_position_filter = (
        Q(first_position__icontains=duo_position[0]) |
        Q(first_position__icontains=duo_position[1]))
      elif duo_position_size == 3:
        duo_position_filter = (
        Q(first_position__icontains=duo_position[0]) |
        Q(first_position__icontains=duo_position[1]) |
        Q(first_position__icontains=duo_position[2]))
      elif duo_position_size == 4:
        duo_position_filter = (
        Q(first_position__icontains=duo_position[0]) |
        Q(first_position__icontains=duo_position[1]) |
        Q(first_position__icontains=duo_position[2]) |
        Q(first_position__icontains=duo_position[3]))
      else:
        duo_position_filter = (
        Q(first_position__icontains=duo_position[0]) |
        Q(first_position__icontains=duo_position[1]) |
        Q(first_position__icontains=duo_position[2]) |
        Q(first_position__icontains=duo_position[3]) |
        Q(first_position__icontains=duo_position[4]))

      duo_all = UserPref.objects.filter(
        duo_position_filter & 
        Q(duo_position__icontains=user_db.first_position[0]))[:100]
      duo_list = []
      for duo in duo_all:
        duo_list.append(duo.user_id)

      # Converter data para usar
      d_r = user_db.duo_refused
      d_a = user_db.duo_accepted
      d_r = d_r.split(',')
      d_a = d_a.split(',')

      for i in range(0,len(d_r)):
        d_r[i] = int(d_r[i])
      for i in range(0,len(d_a)):
        d_a[i] = int(d_a[i])
      d_r = list(d_r)
      d_a = list(d_a)
      duo_refused = set(d_r)
      duo_accepted = set(d_a)

      # Tirar os duos que já foram recusados ou aceitos
      duo_subtract = duo_accepted - duo_refused
      result = d_r + d_a
      duo_ids = set(duo_list) - set(result)
      duo_ids = list(duo_ids)

      duo_possible_match = UserPref.objects.filter(user_id=request.user.id)[0].duo_match

      duo_possible_match = duo_possible_match.split(',')
      if len(duo_possible_match) > 1:
        for i in range(0, len(duo_possible_match)):
          duo_possible_match[i] = int(duo_possible_match[i])
        duo_possible_match.remove(0)
        duo_ids = duo_possible_match
        print(duo_ids)

      # Deixar os que sobraram
      duo_filter = UserPref.objects.filter(user_id__in=duo_ids)

      # Shuffle list
      duo_filter_list = duo_filter
      shuffled_list = []
      for d in duo_filter_list:
        shuffled_list.append(d)

      shuffle(shuffled_list)

      profile_icon_url = None
      if shuffled_list != []:
        API_KEY = config('API_KEY')
        watcher = LolWatcher(api_key=API_KEY)
        region = 'br1'
        summoner_puuid = shuffled_list[0].user.puuid

        account_info = watcher.summoner.by_puuid(region=region, encrypted_puuid=summoner_puuid)

        summoner_icon = account_info['profileIconId']

        profile_icon_url = f'https://ddragon.leagueoflegends.com/cdn/{game_version}/img/profileicon/{summoner_icon}.png'

        rank_info = watcher.league.by_summoner(region=region,encrypted_summoner_id=account_info['id'])

        summoner_tier = 'Unranked'
        if rank_info != []:
          for i in range(0, len(rank_info)):
            if rank_info[i]['queueType'] == 'RANKED_SOLO_5x5':
              summoner_tier = rank_info[i]['tier']

        champion_mastery = watcher.champion_mastery.by_summoner(region=region,encrypted_summoner_id=account_info['id'])

        champion_url = f'http://ddragon.leagueoflegends.com/cdn/{game_version}/data/pt_BR/champion.json'

        champion_list_id = []
        champion_image = []
        if len(champion_mastery) > 0:
          for i in range(0, len(champion_mastery)):
            champion_list_id.append(champion_mastery[i]['championId'])
            champion_list_id[i] = str(champion_list_id[i])

          response = urllib.request.urlopen(champion_url)

          champion_name = []
          input_dict = json.loads(response.read())

          for champion in input_dict['data']:
            key = input_dict['data'][champion]['key']
            for x in champion_list_id:
              if key == x:
                champion_name.append(champion)

          for name in champion_name:
            cname = name
            champion_image_url = f'http://ddragon.leagueoflegends.com/cdn/{game_version}/img/champion/{cname}.png'
            champion_image.append(champion_image_url)
          
          for i in range(0, 3 - len(champion_image)):
            champion_image.append('../static/users/images/icons/no_icon.png')
        else:
          for i in range(0, 3):
            champion_image.append('../static/users/images/icons/no_icon.png')
      else:
        return JsonResponse({
          'card_empty': True,
        })

      return JsonResponse({
        'card_empty': False,
        'card_username': shuffled_list[0].user.username_lol,
        'card_id': shuffled_list[0].user_id,
        'card_image': profile_icon_url,
        'card_bio': shuffled_list[0].bio,
        'card_name': shuffled_list[0].user.first_name,
        'card_position1': shuffled_list[0].first_position,
        'card_position2': shuffled_list[0].second_position,
        'card_filter': shuffled_list[0].duo_position,
        'match_exists': match_exists,
        'summoner_tier': summoner_tier,
        'champion_image': champion_image
        })
    else:
      user_db = UserPref.objects.get(user_id=request.user.id)
      user_filter_db = UserPref.objects.filter(user_id=request.user.id)
      duo_position = user_db.duo_position
      duo_position_size = len(duo_position)
      
      duo_position_filter = None
      if duo_position_size == 1:
        duo_position_filter = (
        Q(first_position__icontains=duo_position[0]))
      elif duo_position_size == 2:
        duo_position_filter = (
        Q(first_position__icontains=duo_position[0]) |
        Q(first_position__icontains=duo_position[1]))
      elif duo_position_size == 3:
        duo_position_filter = (
        Q(first_position__icontains=duo_position[0]) |
        Q(first_position__icontains=duo_position[1]) |
        Q(first_position__icontains=duo_position[2]))
      elif duo_position_size == 4:
        duo_position_filter = (
        Q(first_position__icontains=duo_position[0]) |
        Q(first_position__icontains=duo_position[1]) |
        Q(first_position__icontains=duo_position[2]) |
        Q(first_position__icontains=duo_position[3]))
      else:
        duo_position_filter = (
        Q(first_position__icontains=duo_position[0]) |
        Q(first_position__icontains=duo_position[1]) |
        Q(first_position__icontains=duo_position[2]) |
        Q(first_position__icontains=duo_position[3]) |
        Q(first_position__icontains=duo_position[4]))

      duo_all = UserPref.objects.filter(
        duo_position_filter & 
        Q(duo_position__icontains=user_db.first_position[0]))[:100]
        
      duo_list = []
      for duo in duo_all:
        duo_list.append(duo.user_id)

      # Converter data para usar
      d_r = user_db.duo_refused
      d_a = user_db.duo_accepted
      d_r = d_r.split(',')
      d_a = d_a.split(',')
      for i in range(0,len(d_r)):
        d_r[i] = int(d_r[i])
      for i in range(0,len(d_a)):
        d_a[i] = int(d_a[i])
      d_r = list(d_r)
      d_a = list(d_a)
      duo_refused = set(d_r)
      duo_accepted = set(d_a)
      
      # Tirar os duos que já foram recusados ou aceitos
      duo_subtract = duo_accepted - duo_refused
      result = list(duo_refused) + list(duo_subtract)
      duo_ids = set(duo_list) - set(result)
      duo_ids = list(duo_ids)

      duo_possible_match = UserPref.objects.filter(user_id=request.user.id)[0].duo_match

      duo_possible_match = duo_possible_match.split(',')
      if len(duo_possible_match) > 1:
        for i in range(0, len(duo_possible_match)):
          duo_possible_match[i] = int(duo_possible_match[i])
        duo_possible_match.remove(0)
        duo_ids = duo_possible_match
        print(duo_ids)
      print("Possíveis duos",duo_ids)
      # Deixar os que sobraram
      duo_filter = UserPref.objects.filter(user_id__in=duo_ids)
      # Shuffle list
      duo_filter_list = duo_filter
      shuffled_list = []

      for d in duo_filter_list:
        shuffled_list.append(d)
      
      shuffle(shuffled_list)

      profile_icon_url = None
      summoner_tier = 'Unranked'
      champion_image = []
      if shuffled_list != []:
        API_KEY = config('API_KEY')
        watcher = LolWatcher(api_key=API_KEY)
        region = 'br1'
        summoner_puuid = shuffled_list[0].user.puuid

        account_info = watcher.summoner.by_puuid(region=region, encrypted_puuid=summoner_puuid)

        summoner_icon = account_info['profileIconId']

        profile_icon_url = f'https://ddragon.leagueoflegends.com/cdn/{game_version}/img/profileicon/{summoner_icon}.png'

        rank_info = watcher.league.by_summoner(region=region,encrypted_summoner_id=account_info['id'])

        if rank_info != []:
          for i in range(0, len(rank_info)):
            if rank_info[i]['queueType'] == 'RANKED_SOLO_5x5':
              summoner_tier = rank_info[i]['tier']

        champion_mastery = watcher.champion_mastery.by_summoner(region=region,encrypted_summoner_id=account_info['id'])

        champion_url = f'http://ddragon.leagueoflegends.com/cdn/{game_version}/data/pt_BR/champion.json'
        
        champion_list_id = []
        if len(champion_mastery) > 0:
          champ_pool = 0
          if len(champion_mastery) >= 3:
            champ_pool = 3
          elif len(champion_mastery) == 2:
            champ_pool = 2
          else:
            champ_pool = 1
          for i in range(0, champ_pool):
            champion_list_id.append(champion_mastery[i]['championId'])
            champion_list_id[i] = str(champion_list_id[i])

          response = urllib.request.urlopen(champion_url)

          champion_name = []
          input_dict = json.loads(response.read())

          for champion in input_dict['data']:
            key = input_dict['data'][champion]['key']
            for x in champion_list_id:
              if key == x:
                champion_name.append(champion)
          print(champion_name)
          for name in champion_name:
            cname = name
            champion_image_url = f'http://ddragon.leagueoflegends.com/cdn/{game_version}/img/champion/{cname}.png'
            champion_image.append(champion_image_url)
          
          for i in range(0, 3 - len(champion_image)):
            champion_image.append('../static/users/images/icons/no_icon.png')
        else:
          for i in range(0, 3):
            champion_image.append('../static/users/images/icons/no_icon.png')

      print(profile_icon_url)
      return render(request, 'cards.html', {
        'duo_filter': shuffled_list,
        'profile_icon_url': profile_icon_url,
        'summoner_tier': summoner_tier,
        'champion_image': champion_image
        })
  else:
    return redirect('home')

def preferences(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
      form = UserPreferences(request.POST)

      # Get form data
      bio = form['bio'].value().strip()
      bio = " ".join(bio.split())
      birth = form['birth'].value()
      birth = birth.split('/')
      birth = birth[2]+'-'+birth[1]+'-'+birth[0]

      duo_position = form['duo_position'].value()
      first_position = form['first_position'].value()
      second_position = form['second_position'].value()
      gender = form['gender'].value()
      print(birth)

      if len(duo_position) == 0:
        return render(request, 'preferences.html', {'form': form, 'error': 'Você deve escolher pelo menos uma posição!'})
      elif len(bio) > 150 or len(bio) < 50:
        return render(request, 'preferences.html', {'form': form, 'error': 'A bio deve ter no mínimo 50 caracters e no máximo 150 caracters!'})
      elif first_position == second_position:
        return render(request, 'preferences.html', {'form': form, 'error': 'A primeira posição deve ser diferente da segunda posição!'})

      if form.is_valid():
        # Creating or updating
        up, created = UserPref.objects.update_or_create(
          user=request.user,
          defaults={
            'bio': bio, 
            'birth': birth,
            'duo_position': duo_position,
            'first_position': first_position,
            'second_position': second_position,
            'gender': gender,
            }
          )
        # Prevent user card appear
        user = UserPref.objects.filter(user_id=request.user.id)
        drsize = len(user[0].duo_refused)
        if drsize == 1:
          user.update(duo_refused=request.user.id)

        return redirect('/profile')
    else:
      exists_pref = UserPref.objects.filter(user=request.user).exists()
      up = None
      form = None
      if exists_pref:
        up = UserPref.objects.get(user=request.user)
        form = UserPreferences(initial={
          'bio': up.bio, 
          'birth': up.birth, 
          'duo_position': up.duo_position, 
          'first_position': up.first_position,
          'second_position': up.second_position,
          'gender': up.gender,
          })
      else:
        form = UserPreferences()
      return render(request, 'preferences.html', {'form': form})
  else:
    return redirect('home')


def delete_account(request):
  if request.method == 'POST':
    delete_account_status = request.POST.get('delete_account')
    if delete_account_status == 'True':

      my_id = request.user.id
      my_user = UserPref.objects.filter(user_id=my_id)[0]

      my_matches = my_user.match.split(',')
      for i in range(0, len(my_matches)):
        my_matches[i] = int(my_matches[i])

      match_id_list = []
      for item in my_matches:
        match_id_list.append(item)
      match_id_list.remove(0)

      my_matches = UserPref.objects.filter(user_id__in=match_id_list)
      new_duo_match = '0'
      for match in my_matches:
        duo_match = match.match.split(',')
        for i in range(0, len(duo_match)):
          duo_match[i] = int(duo_match[i])
          
        duo_match.remove(my_id)
        duo_match.remove(0)
        if len(duo_match) > 0:
          for item in duo_match:
            new_duo_match = new_duo_match + ',' + str(item)

        save_new_match = UserPref.objects.filter(user_id=match.user_id).update(match=new_duo_match)

      delete_user = User.objects.filter(id=my_id).delete()

  return redirect('home')

def clear_matches(request):
  if request.method == 'POST':
    clear_matches = request.POST.get('clear_matches')
    if clear_matches == 'True':
      my_id = request.user.id
      my_user = UserPref.objects.filter(user_id=my_id)[0]

      my_matches = my_user.match.split(',')
      for i in range(0, len(my_matches)):
        my_matches[i] = int(my_matches[i])

      match_id_list = []
      for item in my_matches:
        match_id_list.append(item)
      match_id_list.remove(0)

      my_matches = UserPref.objects.filter(user_id__in=match_id_list)
      new_duo_match = '0'
      for match in my_matches:
        print(match.user.username_lol)
        duo_match = match.match.split(',')
        for i in range(0, len(duo_match)):
          duo_match[i] = int(duo_match[i])
          
        duo_match.remove(my_id)
        duo_match.remove(0)
        if len(duo_match) > 0:
          for item in duo_match:
            new_duo_match = new_duo_match + ',' + str(item)

        save_new_match = UserPref.objects.filter(user_id=match.user_id).update(match=new_duo_match)
        reset_my_matches = UserPref.objects.filter(user_id=my_id).update(match=0)

  return redirect('home')

def clear_refused(request):
  if request.method == 'POST':
    clear_refused = request.POST.get('clear_refused')
    if clear_refused == 'True':
      reset_refused = UserPref.objects.filter(user_id=request.user.id).update(duo_refused=request.user.id)
  return redirect('home')




