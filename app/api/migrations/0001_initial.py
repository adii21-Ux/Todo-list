# Generated by Django 3.2.12 on 2022-02-16 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=255)),
                ('task_description', models.TextField()),
                ('task_time', models.DateTimeField(auto_now_add=True)),
                ('task_iscompleted', models.BooleanField()),
            ],
        ),
    ]
