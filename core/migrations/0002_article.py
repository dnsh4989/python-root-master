# Generated by Django 3.1.7 on 2023-04-19 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=500, null=True)),
                ('image', models.CharField(max_length=255)),
                ('content', models.TextField(max_length=5000, null=True)),
            ],
        ),
    ]
