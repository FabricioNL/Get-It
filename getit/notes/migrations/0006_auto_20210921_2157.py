# Generated by Django 3.2.7 on 2021-09-22 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20210921_0847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='note',
        ),
        migrations.AddField(
            model_name='note',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notes.tag'),
        ),
    ]
