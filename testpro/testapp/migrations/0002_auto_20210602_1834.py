# Generated by Django 3.2.3 on 2021-06-02 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watersources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rain', models.TextField(max_length=50)),
                ('lake', models.CharField(max_length=50)),
                ('well', models.CharField(max_length=50)),
                ('canal', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lastname',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='fisrtname',
        ),
        migrations.AddField(
            model_name='user',
            name='aadhar',
            field=models.CharField(max_length=12, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_Tenant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_owner',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='reg',
            field=models.CharField(choices=[('O', 'Owner'), ('R', 'Renter')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=255)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=255)),
                ('images', models.FileField(upload_to=None)),
                ('price', models.IntegerField(unique=True)),
                ('description', models.CharField(max_length=255)),
                ('type_of_soil', models.CharField(choices=[('c', 'Clay'), ('s', 'silt'), ('ch', 'chalk'), ('p', 'peat'), ('l', 'loam')], max_length=2)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.user')),
                ('water', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.watersources')),
            ],
        ),
    ]
