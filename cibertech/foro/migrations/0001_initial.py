# Generated by Django 4.2.6 on 2023-12-16 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('nameCreator', models.CharField(max_length=255)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('nameCreator', models.CharField(max_length=255)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('categoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messageCa', to='foro.category')),
            ],
        ),
    ]
