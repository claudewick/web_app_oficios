# Generated by Django 4.1 on 2022-10-10 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficios', '0006_alter_authority_institution_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentol',
            name='delivery_date_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data de Envio'),
        ),
    ]
