# Generated by Django 3.2.6 on 2021-08-22 19:32

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_alter_userpreferences_duo_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpreferences',
            name='first_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('top', 'Top'), ('jg', 'Caçador'), ('adc', 'Atirador'), ('sup', 'Suporte'), ('mid', 'Mid')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='duo_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('top', 'Top'), ('jg', 'Caçador'), ('adc', 'Atirador'), ('sup', 'Suporte'), ('mid', 'Mid')], default=None, max_length=18),
        ),
    ]