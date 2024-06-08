# Generated by Django 5.0.6 on 2024-06-05 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_remove_login_db_conform_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Product_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('Total_Price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
