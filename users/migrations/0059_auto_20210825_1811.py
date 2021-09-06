# Generated by Django 3.2.6 on 2021-08-25 21:11

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0058_auto_20210825_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreferences',
            name='duo_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('mid', 'Mid'), ('adc', 'Atirador'), ('jg', 'Caçador'), ('top', 'Top'), ('sup', 'Suporte')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='first_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('mid', 'Mid'), ('adc', 'Atirador'), ('jg', 'Caçador'), ('top', 'Top'), ('sup', 'Suporte')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='gender',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('F', 'Feminino'), ('O', 'Outro'), ('M', 'Masculino')], default=None, max_length=5),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='second_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('mid', 'Mid'), ('adc', 'Atirador'), ('jg', 'Caçador'), ('top', 'Top'), ('sup', 'Suporte')], default=None, max_length=18),
        ),
    ]