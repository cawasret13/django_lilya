# Generated by Django 4.1.1 on 2022-10-09 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getData', '0009_products_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='count',
        ),
        migrations.AddField(
            model_name='products',
            name='idV',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
