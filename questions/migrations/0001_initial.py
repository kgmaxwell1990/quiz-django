# Generated by Django 2.0.6 on 2018-08-07 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=250, null=True)),
                ('correct_answer', models.CharField(blank=True, max_length=250, null=True)),
                ('wrong_answer1', models.CharField(blank=True, max_length=250, null=True)),
                ('wrong_answer2', models.CharField(blank=True, max_length=250, null=True)),
                ('wrong_answer3', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
