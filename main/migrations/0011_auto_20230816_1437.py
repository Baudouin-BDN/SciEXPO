# Generated by Django 3.1.2 on 2023-08-16 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_ecole_alter_inscrit_school_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=30)),
                ('image', models.ImageField(null=True, upload_to='images/ABOUT_US')),
            ],
        ),
        migrations.AlterField(
            model_name='ecole',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='etanteleve',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='inscrit',
            name='cover_image',
            field=models.ImageField(default='images/default_img/cover_default.jpg', upload_to='images', verbose_name='Image de couverture'),
        ),
        migrations.AlterField(
            model_name='inscrit',
            name='function_in_school',
            field=models.CharField(choices=[('Eleve', 'Elève'), ('Professeur', 'Professeur'), ('Directeur', 'Directeur'), ('Prefet', 'Préfet'), ('Secretaire', 'Secretaire'), ('Ancien_eleve', 'Ancien élève'), ('-', '-')], default='-', max_length=40, verbose_name='Statut'),
        ),
        migrations.AlterField(
            model_name='inscrit',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='option',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
