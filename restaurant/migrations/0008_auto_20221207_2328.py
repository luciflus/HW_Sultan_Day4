# Generated by Django 3.2 on 2022-12-07 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_auto_20221207_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.client'),
        ),
        migrations.AlterField(
            model_name='order',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.worker'),
        ),
    ]