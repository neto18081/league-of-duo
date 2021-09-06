# Generated by Django 3.2.6 on 2021-08-24 19:39

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0052_auto_20210824_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreferences',
            name='duo_position',
            field=models.IntegerField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='first_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('sup', 'Suporte'), ('jg', 'Caçador'), ('adc', 'Atirador'), ('top', 'Top'), ('mid', 'Mid')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='gender',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], default=None, max_length=5),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='second_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('sup', 'Suporte'), ('jg', 'Caçador'), ('adc', 'Atirador'), ('top', 'Top'), ('mid', 'Mid')], default=None, max_length=18),
        ),
    ]