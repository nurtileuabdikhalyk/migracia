# Generated by Django 3.2.9 on 2022-05-24 17:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_news_yout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jer',
            name='image',
        ),
        migrations.RemoveField(
            model_name='jer',
            name='slug',
        ),
        migrations.AddField(
            model_name='jer',
            name='rayon',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Аудан'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jer',
            name='village',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Ауыл'),
            preserve_default=False,
        ),
    ]
