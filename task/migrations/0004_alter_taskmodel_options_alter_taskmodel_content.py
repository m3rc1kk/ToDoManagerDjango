# Generated by Django 4.2 on 2023-04-17 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_taskmodel_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taskmodel',
            options={'ordering': ['complete_date']},
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='content',
            field=models.CharField(max_length=25, null=True, verbose_name='Задача'),
        ),
    ]
