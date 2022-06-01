# Generated by Django 3.2.9 on 2022-05-29 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vakancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=500, verbose_name='Аймақ')),
                ('qyzmet', models.TextField(verbose_name='Қызмет')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансиялар',
                'db_table': 'vakancia',
            },
        ),
    ]
