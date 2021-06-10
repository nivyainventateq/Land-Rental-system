# Generated by Django 3.2.3 on 2021-06-08 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_auto_20210608_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('roles_id', models.AutoField(primary_key=True, serialize=False)),
                ('roles_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Soiltypes',
            fields=[
                ('soil_id', models.AutoField(primary_key=True, serialize=False)),
                ('soil_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='property',
            old_name='water',
            new_name='water_id',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_owner',
            new_name='is_landowner',
        ),
        migrations.RemoveField(
            model_name='property',
            name='type_of_soil',
        ),
        migrations.RemoveField(
            model_name='watersources',
            name='id',
        ),
        migrations.AddField(
            model_name='watersources',
            name='watersource_id',
            field=models.AutoField(default=2, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
        migrations.AddField(
            model_name='property',
            name='soil_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.soiltypes'),
        ),
        migrations.AddField(
            model_name='user',
            name='roles_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.roles'),
        ),
    ]
