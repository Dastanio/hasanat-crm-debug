# Generated by Django 3.1.2 on 2020-11-17 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201031_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='change_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='created_by',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='change_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_by',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
