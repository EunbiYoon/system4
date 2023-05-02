# Generated by Django 3.2.12 on 2023-05-01 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0009_remove_comment_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment_body',
        ),
        migrations.AddField(
            model_name='comment',
            name='commenter_name',
            field=models.CharField(default='eunbi', max_length=200),
            preserve_default=False,
        ),
    ]
