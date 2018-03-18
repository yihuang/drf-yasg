# Generated by Django 2.0.1 on 2018-02-26 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'first'), (2, 'second'), (3, 'third'), (7, 'seven'), (8, 'eight')], help_text='IntegerField declared on model with choices=(...) and exposed via ModelSerializer', null=True),
        ),
    ]