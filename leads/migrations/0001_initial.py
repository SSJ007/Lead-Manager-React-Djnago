# Generated by Django 3.1.1 on 2020-09-25 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, verbose_name='Name')),
                ('email', models.EmailField(max_length=254)),
                ('document', models.CharField(max_length=20, verbose_name='Document')),
                ('phone', models.CharField(max_length=20)),
                ('registrationDate', models.DateField(auto_now_add=True, verbose_name='Registration Date')),
            ],
        ),
    ]
