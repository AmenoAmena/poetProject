# Generated by Django 4.2.7 on 2024-04-12 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='poet_author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='poets_shown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poetName', models.CharField(max_length=60)),
                ('poetContext', models.TextField(max_length=4000)),
                ('popularity', models.PositiveIntegerField(default=0)),
                ('poetAuthor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poetsShown.poet_author')),
            ],
        ),
    ]
