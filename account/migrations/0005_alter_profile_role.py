# Generated by Django 3.2.16 on 2023-05-30 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20230530_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.IntegerField(choices=[(1, 'Petinggi Hawariyyun'), (2, 'Sekretaris'), (3, 'Bendahara'), (4, 'PSDM'), (5, 'Media Komunikasi'), (6, 'Anggota')], default=6),
        ),
    ]