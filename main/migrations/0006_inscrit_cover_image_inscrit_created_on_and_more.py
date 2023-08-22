# Generated by Django 4.1.7 on 2023-08-12 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_inscrit_birth_date_inscrit_current_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscrit',
            name='cover_image',
            field=models.ImageField(default='images/defult_img/cover_default.jpg', upload_to='images'),
        ),
        migrations.AddField(
            model_name='inscrit',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='inscrit',
            name='about',
            field=models.TextField(blank=True, null=True, verbose_name='A propos de vous'),
        ),
        migrations.AlterField(
            model_name='inscrit',
            name='current_city',
            field=models.CharField(max_length=20, null=True, verbose_name='Ville ou territoire actuel(le)'),
        ),
    ]
