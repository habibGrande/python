# Generated by Django 4.2.7 on 2023-11-26 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='author', to='books_authors_app.book'),
        ),
    ]