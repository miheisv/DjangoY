# Generated by Django 3.2.4 on 2022-11-25 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_feedback_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='text',
            field=models.TextField(default='', help_text='Введите текст'),
        ),
    ]
