# Generated by Django 5.1.2 on 2024-10-28 18:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='accounts.user')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='SponsorshipRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pendente'), ('accepted', 'Aceito'), ('rejected', 'Rejeitado')], default='pending', max_length=20)),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsorship_requests', to='accounts.paralympicswimmerprofile')),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsorship_requests', to='accounts.sponsorprofile')),
            ],
        ),
    ]