# Generated by Django 2.1.5 on 2019-02-04 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0005_quiz'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='example_1_pinin',
            new_name='example_1_pinyin',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='example_2_pinin',
            new_name='example_2_pinyin',
        ),
    ]
