# Generated by Django 3.2.6 on 2021-08-22 20:58

import django.contrib.auth.validators
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_auto_20210822_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password2',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='duo_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('jg', 'Caçador'), ('sup', 'Suporte'), ('adc', 'Atirador'), ('mid', 'Mid'), ('top', 'Top')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='first_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('jg', 'Caçador'), ('sup', 'Suporte'), ('adc', 'Atirador'), ('mid', 'Mid'), ('top', 'Top')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='gender',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], default=None, max_length=5),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='second_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('jg', 'Caçador'), ('sup', 'Suporte'), ('adc', 'Atirador'), ('mid', 'Mid'), ('top', 'Top')], default=None, max_length=18),
        ),
    ]