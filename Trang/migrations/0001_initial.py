# Generated by Django 2.0.4 on 2019-02-12 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trangle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.IntegerField(default=0)),
                ('b', models.IntegerField(default=0)),
                ('c', models.IntegerField(default=0)),
                ('output', models.CharField(choices=[(1, 'Scalene'), (1, 'Equilateral'), (1, 'Isosceles'), (1, 'Incorrect')], default=1, max_length=100)),
            ],
        ),
    ]