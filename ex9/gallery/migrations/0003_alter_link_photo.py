# Generated by Django 3.2.3 on 2021-05-29 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='photo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='link', to='gallery.photo'),
        ),
    ]
