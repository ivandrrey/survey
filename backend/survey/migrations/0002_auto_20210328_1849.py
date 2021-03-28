# Generated by Django 2.2.4 on 2021-03-28 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='description',
            field=models.TextField(blank=True, max_length=1020, null=True),
        ),
        migrations.AlterField(
            model_name='surveyresult',
            name='user_id',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10000, null=True),
        ),
    ]
