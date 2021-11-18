# Generated by Django 3.2.7 on 2021-11-18 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_investment_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='stock',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.stock'),
        ),
        migrations.AlterField(
            model_name='investment',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
