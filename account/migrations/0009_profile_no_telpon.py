# Generated by Django 3.2.16 on 2023-06-02 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20230602_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='no_telpon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
