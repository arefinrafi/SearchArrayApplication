# Generated by Django 4.1.3 on 2022-11-10 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('codingapp', '0002_khojsearch_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='khojsearch',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payload', to=settings.AUTH_USER_MODEL),
        ),
    ]