# Generated by Django 3.1.1 on 2021-12-31 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0013_auto_20211231_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pages.category')),
            ],
        ),
    ]