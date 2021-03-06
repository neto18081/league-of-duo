# Generated by Django 3.2.6 on 2021-09-06 16:58

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0065_auto_20210905_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreferences',
            name='duo_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('adc', 'adc'), ('top', 'top'), ('jg', 'jg'), ('mid', 'mid'), ('sup', 'sup')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='first_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('adc', 'adc'), ('top', 'top'), ('jg', 'jg'), ('mid', 'mid'), ('sup', 'sup')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='gender',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('O', 'Outro'), ('F', 'Feminino'), ('M', 'Masculino')], default=None, max_length=5),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='second_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('adc', 'adc'), ('top', 'top'), ('jg', 'jg'), ('mid', 'mid'), ('sup', 'sup')], default=None, max_length=18),
        ),
    ]
