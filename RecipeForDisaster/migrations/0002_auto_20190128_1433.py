# Generated by Django 2.1.5 on 2019-01-28 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RecipeForDisaster', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='RecipeForDisaster.Recipe'),
        ),
    ]
