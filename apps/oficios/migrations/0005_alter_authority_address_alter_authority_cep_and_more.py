# Generated by Django 4.1 on 2022-10-03 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficios', '0004_alter_receivedol_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authority',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='authority',
            name='cep',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='authority',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='authority',
            name='complement',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Complemento'),
        ),
        migrations.AlterField(
            model_name='authority',
            name='institution',
            field=models.CharField(max_length=200, verbose_name='Órgão/Insituição'),
        ),
        migrations.AlterField(
            model_name='authority',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='authority',
            name='number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='authority',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='authority',
            name='post',
            field=models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Cargo/Função'),
        ),
        migrations.AlterField(
            model_name='authority',
            name='state',
            field=models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceara'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='SP', max_length=2, verbose_name='Estado'),
        ),
    ]
