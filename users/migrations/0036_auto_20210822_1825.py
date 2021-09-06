# Generated by Django 3.2.6 on 2021-08-22 21:25

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0035_auto_20210822_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreferences',
            name='duo_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('adc', 'Atirador'), ('top', 'Top'), ('mid', 'Mid'), ('sup', 'Suporte'), ('jg', 'Caçador')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='first_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('adc', 'Atirador'), ('top', 'Top'), ('mid', 'Mid'), ('sup', 'Suporte'), ('jg', 'Caçador')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='gender',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('O', 'Outro'), ('F', 'Feminino'), ('M', 'Masculino')], default=None, max_length=5),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='second_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('adc', 'Atirador'), ('top', 'Top'), ('mid', 'Mid'), ('sup', 'Suporte'), ('jg', 'Caçador')], default=None, max_length=18),
        ),
    ]