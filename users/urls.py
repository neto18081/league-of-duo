from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
  path('', views.home, name='home'),
  path('login/', LoginView.as_view(template_name='registration/login.html',redirect_authenticated_user=True), name='login'),
  path("register/", views.register, name="register"),
  path("profile/", views.profile, name="profile"),
  path("preferences/", views.preferences, name="preferences"),
  path("cards/", views.cards, name="cards"),
  path('riot.txt/', views.riot, name="riot"),
  path('forgot_password/', views.forgot_password, name="forgot_password"),
  path('confirm_code/', views.confirm_code, name="confirm_code"),

  path('delete_account/', views.delete_account, name="delete_account"),
  path('clear_refused/', views.clear_refused, name="clear_refused"),
  path('clear_matches/', views.clear_matches, name="clear_matches"),
]