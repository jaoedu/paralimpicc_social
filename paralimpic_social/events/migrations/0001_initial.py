# Generated by Django 5.1.2 on 2024-10-28 17:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=200)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
                ('participants', models.ManyToManyField(blank=True, related_name='events_participating', to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField()),
                ('time', models.DurationField(blank=True, null=True)),
                ('notes', models.TextField(blank=True)),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='events.event')),
            ],
        ),
    ]
