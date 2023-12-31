# Generated by Django 4.2.2 on 2023-08-29 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_notifications_date_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'ordering': ['-date_created']},
        ),
        migrations.AddField(
            model_name='feedback',
            name='reply',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='reply_created_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
