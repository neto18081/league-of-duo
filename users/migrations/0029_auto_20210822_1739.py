# Generated by Django 3.2.6 on 2021-08-22 20:39

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_auto_20210822_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='puuid',
            field=models.CharField(default=None, max_length=200, null=True, verbose_name='puuid'),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='duo_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('jg', 'Caçador'), ('mid', 'Mid'), ('sup', 'Suporte'), ('adc', 'Atirador'), ('top', 'Top')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='first_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('jg', 'Caçador'), ('mid', 'Mid'), ('sup', 'Suporte'), ('adc', 'Atirador'), ('top', 'Top')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='gender',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], default=None, max_length=5),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='second_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('jg', 'Caçador'), ('mid', 'Mid'), ('sup', 'Suporte'), ('adc', 'Atirador'), ('top', 'Top')], default=None, max_length=18),
        ),
    ]
