# Generated by Django 5.2 on 2025-04-27 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configapp', '0003_homework_homeworksubmission_homeworkreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'month',
                'verbose_name_plural': 'months',
            },
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'payment type',
                'verbose_name_plural': 'payment types',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment', to='configapp.groupstudent')),
                ('month', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='configapp.month')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='configapp.student')),
                ('payment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='configapp.paymenttype')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
    ]
