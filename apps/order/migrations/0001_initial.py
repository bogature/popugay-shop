# Generated by Django 3.0.3 on 2020-02-09 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_auto_20200209_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('money', models.FloatField(default=0)),
                ('dell', models.BooleanField(default=False)),
                ('product', models.ManyToManyField(to='product.Product')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзина',
            },
        ),
    ]
