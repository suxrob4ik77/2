# Generated by Django 5.2 on 2025-04-27 09:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='davomat',
            options={'ordering': ['-date', '-created_at']},
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('full_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('descriptions', models.CharField(blank=True, max_length=500, null=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='configapp.student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
