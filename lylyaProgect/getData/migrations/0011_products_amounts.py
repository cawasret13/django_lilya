# Generated by Django 4.1.1 on 2022-10-09 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getData', '0010_remove_products_count_products_idv'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='amounts',
            field=models.IntegerField(null=True),
        ),
    ]
