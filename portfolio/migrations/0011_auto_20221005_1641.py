# Generated by Django 3.2.9 on 2022-10-05 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20221004_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='category',
            field=models.CharField(choices=[('Book Chapters', 'Book Chapters'), ('Conference', 'Conference'), ('Journal', 'Journal'), ('International Reports', 'International Reports'), ('Books', 'Books')], default='Journal', max_length=60),
        ),
        migrations.AlterField(
            model_name='reasearch',
            name='category',
            field=models.CharField(choices=[('Conference Presentation', 'Conference Presentation'), ('Invited Talks', 'Invited Talks'), ('Editorial Boards', 'Editorial Boards')], default='Invited Talks', max_length=60),
        ),
    ]
