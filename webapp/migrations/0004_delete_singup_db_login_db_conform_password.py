# Generated by Django 5.0.6 on 2024-06-04 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_remove_singup_db_confirm'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Singup_db',
        ),
        migrations.AddField(
            model_name='login_db',
            name='conform_password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
