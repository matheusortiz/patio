# Generated by Django 2.2.1 on 2019-05-30 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('remocoes', '0002_auto_20190530_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remocao',
            name='liberacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='remocoes.Liberacao'),
        ),
    ]
