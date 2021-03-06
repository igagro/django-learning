# Generated by Django 2.1.4 on 2018-12-11 09:27

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import localflavor.us.models
import university.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('state', localflavor.us.models.USStateField(blank=True, max_length=2, null=True)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('logo_url', models.ImageField(blank=True, null=True, upload_to=university.models.upload_logo_image)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UniversitySchools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main_school', models.BooleanField(null=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.University')),
            ],
        ),
        migrations.AddField(
            model_name='university',
            name='schools',
            field=models.ManyToManyField(related_name='universities', through='university.UniversitySchools', to='school.School'),
        ),
    ]
