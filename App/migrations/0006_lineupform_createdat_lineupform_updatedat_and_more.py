# Generated by Django 5.2.1 on 2025-05-29 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_users_combinedfield'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineupform',
            name='CreatedAt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='lineupform',
            name='UpdatedAt',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='saileddata',
            name='CreatedAt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='saileddata',
            name='UpdatedAt',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
