# Generated by Django 5.1.7 on 2025-05-24 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_lineupform_port_berth_form_saileddata'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='CombinedField',
            field=models.CharField(default='', max_length=80),
        ),
    ]
