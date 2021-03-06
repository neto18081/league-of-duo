# Generated by Django 3.2.6 on 2021-08-23 19:30

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0048_auto_20210823_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreferences',
            name='duo_accepted',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='duo_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('adc', 'Atirador'), ('jg', 'Caçador'), ('top', 'Top'), ('mid', 'Mid'), ('sup', 'Suporte')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='duo_refused',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='first_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('adc', 'Atirador'), ('jg', 'Caçador'), ('top', 'Top'), ('mid', 'Mid'), ('sup', 'Suporte')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='gender',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('O', 'Outro')], default=None, max_length=5),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='second_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('adc', 'Atirador'), ('jg', 'Caçador'), ('top', 'Top'), ('mid', 'Mid'), ('sup', 'Suporte')], default=None, max_length=18),
        ),
    ]
