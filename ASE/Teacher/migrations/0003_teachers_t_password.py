# Generated by Django 2.1.3 on 2018-11-16 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0002_auto_20181116_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='T_password',
            field=models.CharField(default='password123', max_length=50),
            preserve_default=False,
        ),
    ]
