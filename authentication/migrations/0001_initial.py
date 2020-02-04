# Generated by Django 3.0.2 on 2020-02-04 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.IntegerField()),
                ('acheivements', models.CharField(max_length=200)),
                ('stream', models.CharField(max_length=200)),
                ('url', models.URLField(max_length=1000)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.IntegerField()),
                ('acheivements', models.CharField(max_length=200)),
                ('stream', models.CharField(max_length=200)),
                ('url', models.URLField(max_length=1000)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Acheivement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acheivement', models.CharField(max_length=200)),
                ('id_of_professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.Professor')),
            ],
        ),
    ]
