# Generated by Django 4.1.7 on 2023-08-11 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_eleve_id_alter_inscrit_function_in_school_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscrit',
            name='photo',
            field=models.ImageField(default='photos/default.jpg', null=True, upload_to='photos'),
        ),
    ]