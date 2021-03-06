# Generated by Django 3.2.6 on 2021-08-23 16:16

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0047_auto_20210823_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreferences',
            name='duo_accepted',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='duo_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('mid', 'Mid'), ('sup', 'Suporte'), ('top', 'Top'), ('jg', 'Caçador'), ('adc', 'Atirador')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='duo_refused',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='first_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('mid', 'Mid'), ('sup', 'Suporte'), ('top', 'Top'), ('jg', 'Caçador'), ('adc', 'Atirador')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='gender',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('O', 'Outro'), ('M', 'Masculino'), ('F', 'Feminino')], default=None, max_length=5),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='second_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('mid', 'Mid'), ('sup', 'Suporte'), ('top', 'Top'), ('jg', 'Caçador'), ('adc', 'Atirador')], default=None, max_length=18),
        ),
    ]
