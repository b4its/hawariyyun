# Generated by Django 3.2.16 on 2023-06-04 02:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='jawaban_pilgan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jawab', models.CharField(blank=True, max_length=500, null=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='survei',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomor1', models.TextField(blank=True, max_length=1000, null=True)),
                ('nomor2', models.TextField(blank=True, max_length=1000, null=True)),
                ('nomor3', models.TextField(blank=True, max_length=1000, null=True)),
                ('nomor5', models.TextField(blank=True, max_length=1000, null=True)),
                ('nomor6', models.TextField(blank=True, max_length=1000, null=True)),
                ('nomor7', models.TextField(blank=True, max_length=1000, null=True)),
                ('nomor8', models.TextField(blank=True, max_length=1000, null=True)),
                ('nomor9', models.TextField(blank=True, max_length=1000, null=True)),
                ('nomor10', models.TextField(blank=True, max_length=1000, null=True)),
                ('nomor11', models.TextField(blank=True, max_length=1000, null=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('nomor4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jawaban_pilgan', to='survei.jawaban_pilgan', verbose_name='jawab')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jawabku', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]