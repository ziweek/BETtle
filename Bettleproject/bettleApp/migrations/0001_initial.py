# Generated by Django 4.0.4 on 2022-05-28 08:59

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
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstMember', models.CharField(max_length=200)),
                ('seocondMember', models.CharField(max_length=200)),
                ('thirdMember', models.CharField(max_length=200)),
                ('fourthMember', models.CharField(max_length=200)),
                ('Tier', models.CharField(max_length=100)),
                ('bulletBet', models.IntegerField(default=0)),
                ('matchDates', models.CharField(max_length=500, null=True)),
                ('hostUser', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, related_name='hostUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
