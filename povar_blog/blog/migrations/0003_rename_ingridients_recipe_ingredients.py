# Generated by Django 4.0.6 on 2022-07-11 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingridients',
            new_name='ingredients',
        ),
    ]
