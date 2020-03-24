# Generated by Django 3.0.3 on 2020-02-23 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HexMap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hex',
            name='bottomBorderTile',
            field=models.CharField(default='standard', max_length=10),
        ),
        migrations.AlterField(
            model_name='hex',
            name='bottomLeftBorderTile',
            field=models.CharField(default='standard', max_length=10),
        ),
        migrations.AlterField(
            model_name='hex',
            name='bottomRightBorderTile',
            field=models.CharField(default='standard', max_length=10),
        ),
        migrations.AlterField(
            model_name='hex',
            name='leftBorderTile',
            field=models.CharField(default='standard', max_length=10),
        ),
        migrations.AlterField(
            model_name='hex',
            name='rightBorderTile',
            field=models.CharField(default='standard', max_length=10),
        ),
        migrations.AlterField(
            model_name='hex',
            name='topBorderTile',
            field=models.CharField(default='standard', max_length=10),
        ),
        migrations.AlterField(
            model_name='hex',
            name='topLeftBorderTile',
            field=models.CharField(default='standard', max_length=10),
        ),
        migrations.AlterField(
            model_name='hex',
            name='topRightBorderTile',
            field=models.CharField(default='standard', max_length=10),
        ),
    ]