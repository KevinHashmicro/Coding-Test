# Generated by Django 3.2.5 on 2021-07-29 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.IntegerField()),
                ('second', models.IntegerField()),
                ('res', models.TextField()),
            ],
        ),
    ]
