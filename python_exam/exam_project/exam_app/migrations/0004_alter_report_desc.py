# Generated by Django 4.2.7 on 2023-12-04 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0003_report_delete_dashboard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='desc',
            field=models.CharField(max_length=50),
        ),
    ]
