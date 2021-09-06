# Generated by Django 3.2.6 on 2021-08-23 14:07

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0044_auto_20210823_0847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpreferences',
            name='duo_list',
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='duo_accepted',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='duo_refused',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='duo_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('mid', 'Mid'), ('adc', 'Atirador'), ('jg', 'Caçador'), ('sup', 'Suporte'), ('top', 'Top')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='first_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('mid', 'Mid'), ('adc', 'Atirador'), ('jg', 'Caçador'), ('sup', 'Suporte'), ('top', 'Top')], default=None, max_length=18),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='gender',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('O', 'Outro'), ('M', 'Masculino'), ('F', 'Feminino')], default=None, max_length=5),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='second_position',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('mid', 'Mid'), ('adc', 'Atirador'), ('jg', 'Caçador'), ('sup', 'Suporte'), ('top', 'Top')], default=None, max_length=18),
        ),
    ]
