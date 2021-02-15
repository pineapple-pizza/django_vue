# Generated by Django 3.1.4 on 2020-12-16 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('category', models.CharField(choices=[('coffee', 'coffee'), ('snacks', 'snacks'), ('seafood', 'seafood'), ('biscuits', 'biscuits'), ('french_cheese', 'french_cheese')], max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('url', models.TextField()),
                ('nutrition_grade', models.CharField(max_length=255)),
            ],
        ),
    ]