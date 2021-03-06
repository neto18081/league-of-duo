# Generated by Django 3.2.6 on 2021-08-22 20:18

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_auto_20210822_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='puuid',
            field=models.CharField(default=None, max_length=200, verbose_name='puuid'),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='duo_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('top', 'Top'), ('jg', 'Caçador'), ('mid', 'Mid'), ('sup', 'Suporte'), ('adc', 'Atirador')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='first_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('top', 'Top'), ('jg', 'Caçador'), ('mid', 'Mid'), ('sup', 'Suporte'), ('adc', 'Atirador')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='second_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('top', 'Top'), ('jg', 'Caçador'), ('mid', 'Mid'), ('sup', 'Suporte'), ('adc', 'Atirador')], default=None, max_length=18),
        ),
    ]
