# Generated by Django 4.2.6 on 2023-12-16 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='noteBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookTitle', models.CharField(max_length=100)),
                ('bookLink', models.TextField()),
                ('image', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('nameCreator', models.CharField(max_length=255)),
            ],
        ),
    ]
