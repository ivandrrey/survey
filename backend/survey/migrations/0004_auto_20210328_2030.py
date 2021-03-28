# Generated by Django 2.2.4 on 2021-03-28 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20210328_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveycontent',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_questions', to='survey.Survey'),
        ),
        migrations.AlterField(
            model_name='surveyresult',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Survey'),
        ),
    ]