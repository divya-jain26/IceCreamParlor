# Generated by Django 3.0.8 on 2020-07-18 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parlor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icecreame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('desc', models.TextField()),
                ('Img', models.ImageField(upload_to='images/')),
                ('price', models.FloatField()),
            ],
        ),
    ]
