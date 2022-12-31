# Generated by Django 4.1.4 on 2022-12-31 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transaction', '0002_alter_mas_trans_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='mas_trans',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Groups_trans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100, unique=True)),
                ('desc', models.CharField(max_length=500)),
                ('no_of_per', models.IntegerField(default=0)),
                ('amount_pp', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('grp_made_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grp_made_by', to=settings.AUTH_USER_MODEL)),
                ('grp_members', models.ManyToManyField(related_name='grp_member', to=settings.AUTH_USER_MODEL)),
                ('grp_trans_made_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grp_trans_made_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
