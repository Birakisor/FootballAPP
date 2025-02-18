# Generated by Django 5.1.1 on 2024-09-11 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0009_rename_score_away_match_goal_remove_match_score_home'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='goal',
            new_name='awayTeam_goal',
        ),
        migrations.AddField(
            model_name='match',
            name='homeTeam_goal',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
