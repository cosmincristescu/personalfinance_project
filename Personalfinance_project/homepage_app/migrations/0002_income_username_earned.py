# Generated by Django 2.1.3 on 2019-12-17 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='username_earned',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
