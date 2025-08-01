# Generated by Django 5.2.4 on 2025-07-19 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_note_voice_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='note_images/'),
        ),
        migrations.AddField(
            model_name='note',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
