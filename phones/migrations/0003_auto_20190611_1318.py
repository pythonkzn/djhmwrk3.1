# Generated by Django 2.2.2 on 2019-06-11 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_auto_20190611_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='op_s',
            field=models.CharField(choices=[('android', 'android'), ('windows', 'windows'), ('ios', 'ios')], max_length=50),
        ),
    ]
