# Generated by Django 3.1.6 on 2021-02-03 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_extendeduser'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='email',
            field=models.EmailField(default='abc@domain.com', max_length=54),
        ),
    ]
