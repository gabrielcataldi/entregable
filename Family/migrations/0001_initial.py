# Generated by Django 4.0.4 on 2022-05-28 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=59)),
                ('edad', models.IntegerField()),
                ('fecha_nac', models.DateField()),
            ],
        ),
    ]
