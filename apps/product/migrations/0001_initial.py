# Generated by Django 3.0.3 on 2020-02-09 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Категорії',
                'verbose_name_plural': 'Категорії',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('small_description', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('money', models.FloatField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Category')),
            ],
            options={
                'verbose_name': 'Програми',
                'verbose_name_plural': 'Програми',
            },
        ),
    ]
