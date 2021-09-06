from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.forms.widgets import CheckboxSelectMultiple, RadioSelect, Textarea
from .models import User, UserPreferences
from django import forms

class UserPreferences(forms.Form):
  POSITION_CHOICES = (
    ('top', ''),
    ('jg', ''),
    ('mid', ''),
    ('adc', ''),
    ('sup', '')
  )

  GENDER = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outro')
  )

  bio = forms.CharField(widget=Textarea())
  birth = forms.DateField(label="Data de nascimento", widget=forms.SelectDateWidget(years=range(1960, 2022)), initial='2000')
  duo_position = forms.MultipleChoiceField(label='Qual posição você procura em um duo', widget=CheckboxSelectMultiple(), choices=POSITION_CHOICES)
  first_position = forms.ChoiceField(widget=RadioSelect(), label='Sua posição primária', choices=POSITION_CHOICES)
  second_position = forms.ChoiceField(widget=RadioSelect(), label='Sua posição secundária', choices=POSITION_CHOICES)
  gender = forms.ChoiceField(widget=RadioSelect(), label='Gênero', choices=GENDER)

  class Meta(forms.Form):
    model = UserPreferences
    fields = (
      'bio',
      'birth',
      'duo_position'
    )

class UserLogin(AuthenticationForm):
  class Meta(AuthenticationForm):
    model = User
    fields = (
      'username',
      'password'
    )

    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['username'].label = 'Usuário/Email'
      self.fields['password'].label = 'Senha'

class UserCreationForm(UserCreationForm):
  password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(),
    )
  password2 = forms.CharField(
      widget=forms.PasswordInput(),
      strip=False,
  )
  class Meta(UserCreationForm):
    model = User
    fields = (
      'username',
      'username_lol',
      'first_name',
      'email',
      'password1',
      'password2'
    )

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['first_name'].label = 'Seu nome'
    self.fields['username_lol'].label = 'Usuário no LOL'
    self.fields['email'].label = 'Email'
    self.fields['password1'].label = 'Senha'
    self.fields['password2'].label = 'Confirmar senha'

  def save(self, commit=True):
    user = super(UserCreationForm, self).save(commit=False)

    if commit:
      user.save()

    return user

class UserChangeForm(UserChangeForm):
  class Meta(UserChangeForm.Meta):
    model = User