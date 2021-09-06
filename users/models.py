from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField

# Create your models here.
class User(AbstractUser):
  puuid = models.CharField('puuid', max_length=200, blank=True)
  email = models.EmailField('email')
  username_lol = models.CharField('username_lol', max_length=16, default=None)
  first_name = models.CharField('first_name', max_length=16)

class UserPreferences(models.Model):
  POSITION_CHOICES = {
    ('top', 'top'),
    ('jg', 'jg'),
    ('mid', 'mid'),
    ('adc', 'adc'),
    ('sup', 'sup')
  }
  GENDER = {
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outro')
  }

  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userpref', null=True)
  bio = models.TextField(max_length=150)
  birth = models.DateField(default=None)
  duo_position = MultiSelectField(choices=POSITION_CHOICES, default=None)
  first_position = MultiSelectField(choices=POSITION_CHOICES, default=None)
  second_position = MultiSelectField(choices=POSITION_CHOICES, default=None)
  gender = MultiSelectField(choices=GENDER, default=None)
  duo_refused = models.CharField(max_length=500, default=0)
  duo_accepted = models.CharField(max_length=500, default=0)
  duo_match = models.CharField(max_length=500, default=0)
  match = models.CharField(max_length=500, default=0)