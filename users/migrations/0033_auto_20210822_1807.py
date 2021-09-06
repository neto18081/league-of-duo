# Generated by Django 3.2.6 on 2021-08-22 21:07

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0032_auto_20210822_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='USERNAME_FIELD',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=None, max_length=150, verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='duo_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('jg', 'Caçador'), ('sup', 'Suporte'), ('top', 'Top'), ('mid', 'Mid'), ('adc', 'Atirador')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='first_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('jg', 'Caçador'), ('sup', 'Suporte'), ('top', 'Top'), ('mid', 'Mid'), ('adc', 'Atirador')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='gender',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('O', 'Outro'), ('M', 'Masculino'), ('F', 'Feminino')], default=None, max_length=5),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='second_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('jg', 'Caçador'), ('sup', 'Suporte'), ('top', 'Top'), ('mid', 'Mid'), ('adc', 'Atirador')], default=None, max_length=18),
        ),
    ]
