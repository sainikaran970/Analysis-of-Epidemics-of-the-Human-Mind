# Generated by Django 5.0.2 on 2024-03-27 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_contact_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('test1', models.CharField(choices=[('Red', '0'), ('Blue', '1'), ('Green', '2')], max_length=122)),
            ],
        ),
    ]
