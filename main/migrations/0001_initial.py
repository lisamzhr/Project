# Generated by Django 5.2.1 on 2025-05-25 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoodEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mood', models.CharField(max_length=255)),
                ('time', models.DateField(auto_now_add=True)),
                ('feelings', models.TextField()),
                ('mood_intensity', models.IntegerField()),
            ],
        ),
    ]
