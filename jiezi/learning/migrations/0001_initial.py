# Generated by Django 2.1.2 on 2019-01-27 15:47

from django.db import migrations, models
import learning.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('jiezi_id', models.IntegerField(primary_key=True, serialize=False)),
                ('chinese', models.CharField(max_length=1)),
                ('pinyin', models.CharField(max_length=10)),
                ('definition_1', models.CharField(max_length=50)),
                ('definition_2', models.CharField(blank=True, max_length=50, null=True)),
                ('explanation_2', models.CharField(blank=True, max_length=200, null=True)),
                ('definition_3', models.CharField(blank=True, max_length=50, null=True)),
                ('explanation_3', models.CharField(blank=True, max_length=200, null=True)),
                ('pinyin_audio', models.FileField(default='error.mp3', upload_to=learning.models.PathAndRename('/characters', 'pinyin_audio'))),
                ('color_coded_image', models.ImageField(default='default.jpg', upload_to=learning.models.PathAndRename('/characters', 'color_coded_image'))),
                ('stroke_order_image', models.ImageField(default='default.jpg', upload_to=learning.models.PathAndRename('/characters', 'stroke_order_image'))),
                ('mnemonic_explanation', models.CharField(max_length=200)),
                ('mnemonic_1', models.IntegerField(help_text='enter number only')),
                ('mnemonic_2', models.IntegerField(blank=True, help_text="enter number only, if it doens't exits, leave BLANK instead of putting 0", null=True)),
                ('mnemonic_3', models.IntegerField(blank=True, help_text="enter number only, if it doens't exits, leave BLANK instead of putting 0", null=True)),
                ('example_1_word', models.CharField(max_length=5)),
                ('example_1_pinin', models.CharField(max_length=25)),
                ('example_1_character', models.CharField(max_length=50)),
                ('example_1_meaning', models.CharField(max_length=50)),
                ('example_2_word', models.CharField(blank=True, max_length=5, null=True)),
                ('example_2_pinin', models.CharField(blank=True, max_length=25, null=True)),
                ('example_2_character', models.CharField(blank=True, max_length=50, null=True)),
                ('example_2_meaning', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'ordering': ['jiezi_id'],
            },
        ),
        migrations.CreateModel(
            name='CharacterSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('characters', models.ManyToManyField(to='learning.Character')),
            ],
        ),
        migrations.CreateModel(
            name='Radical',
            fields=[
                ('jiezi_id', models.IntegerField(primary_key=True, serialize=False)),
                ('chinese', models.CharField(max_length=1)),
                ('pinyin', models.CharField(max_length=10)),
                ('definition', models.CharField(max_length=50)),
                ('mnemonic_image', models.ImageField(default='default.jpg', upload_to=learning.models.PathAndRename('/radicals', 'mnemonic_image'))),
                ('is_phonetic', models.BooleanField()),
                ('is_semantic', models.BooleanField()),
            ],
            options={
                'ordering': ['jiezi_id'],
            },
        ),
    ]
