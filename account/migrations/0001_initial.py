# Generated by Django 3.1.1 on 2021-11-23 22:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usercategory', to='pages.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
