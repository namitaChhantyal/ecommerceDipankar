# Generated by Django 3.1.7 on 2021-03-10 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_auto_20210310_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='productnameee',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
