# Generated by Django 2.1.4 on 2019-08-30 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190821_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image2',
            field=models.FileField(blank=True, null=True, upload_to='story_pics'),
        ),
        migrations.AddField(
            model_name='post',
            name='image3',
            field=models.FileField(blank=True, null=True, upload_to='story_pics'),
        ),
        migrations.AddField(
            model_name='post',
            name='image4',
            field=models.FileField(blank=True, null=True, upload_to='story_pics'),
        ),
        migrations.AddField(
            model_name='post',
            name='paragraph1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='paragraph2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='paragraph3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='paragraph4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='paragraph5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='paragraph6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='paragraph7',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='paragraph8',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='paragraph9',
            field=models.TextField(blank=True, null=True),
        ),
    ]
