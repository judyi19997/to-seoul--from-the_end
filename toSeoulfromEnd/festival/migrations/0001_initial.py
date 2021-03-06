# Generated by Django 3.0.6 on 2020-06-04 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='festival_M',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('pub_date', models.DateField(blank=True, null=True)),
                ('locate', models.CharField(blank=True, max_length=30, null=True)),
                ('period', models.DateField(blank=True, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='festival/')),
                ('likes', models.IntegerField(blank=True, null=True)),
                ('is_school', models.BooleanField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
