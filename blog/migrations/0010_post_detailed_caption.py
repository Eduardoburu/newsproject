# Generated by Django 2.2.6 on 2019-10-24 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_paragraph10'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='detailed_caption',
            field=models.TextField(blank=True, null=True),
        ),
    ]
