# Generated by Django 3.2.6 on 2021-08-24 13:55

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0050_auto_20210824_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreferences',
            name='duo_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('jg', 'Caçador'), ('top', 'Top'), ('sup', 'Suporte'), ('adc', 'Atirador'), ('mid', 'Mid')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='first_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('jg', 'Caçador'), ('top', 'Top'), ('sup', 'Suporte'), ('adc', 'Atirador'), ('mid', 'Mid')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='gender',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('F', 'Feminino'), ('O', 'Outro'), ('M', 'Masculino')], default=None, max_length=5),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='second_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('jg', 'Caçador'), ('top', 'Top'), ('sup', 'Suporte'), ('adc', 'Atirador'), ('mid', 'Mid')], default=None, max_length=18),
        ),
    ]
