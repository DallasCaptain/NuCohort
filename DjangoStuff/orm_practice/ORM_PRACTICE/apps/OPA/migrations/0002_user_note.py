# Generated by Django 2.2.5 on 2019-10-14 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OPA', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='note',
            field=models.CharField(default='this is the default note', max_length=255),
            preserve_default=False,
        ),
    ]