# Generated by Django 4.1.2 on 2022-10-25 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_skill_social_profile_avatar_profile_verified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='socials',
            field=models.ManyToManyField(blank=True, null=True, to='base.social'),
        ),
    ]
