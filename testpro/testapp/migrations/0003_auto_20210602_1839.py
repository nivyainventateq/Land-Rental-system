# Generated by Django 3.2.3 on 2021-06-02 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20210602_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='reg',
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('1', 'Owner'), ('2', 'Tenant')], max_length=50, null=True),
        ),
    ]
