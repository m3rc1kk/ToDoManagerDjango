# Generated by Django 4.2 on 2023-04-13 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete_date', models.DateTimeField()),
                ('is_complete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'TaskModel',
            },
        ),
    ]
