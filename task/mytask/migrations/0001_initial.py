# Generated by Django 3.2.9 on 2022-11-06 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=25)),
                ('email_id', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('active', models.CharField(default=False, max_length=10)),
            ],
            options={
                'db_table': 'user-form',
            },
        ),
    ]
