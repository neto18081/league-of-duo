# Generated by Django 3.2.6 on 2021-08-22 18:53

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_auto_20210822_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreferences',
            name='duo_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('adc', 'Atirador'), ('jg', 'Caçador'), ('mid', 'Mid'), ('top', 'Top'), ('sup', 'Suporte')], default=None, max_length=18),
        ),
    ]
