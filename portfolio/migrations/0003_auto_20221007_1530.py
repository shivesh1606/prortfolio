# Generated by Django 3.2.9 on 2022-10-07 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20221007_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='category',
            field=models.CharField(choices=[('Conference', 'Conference'), ('Journal', 'Journal'), ('International Reports', 'International Reports'), ('Book Chapters', 'Book Chapters'), ('Books', 'Books')], default='Journal', max_length=60),
        ),
        migrations.AlterField(
            model_name='reasearch',
            name='category',
            field=models.CharField(choices=[('Conference Presentation', 'Conference Presentation'), ('Invited Talks', 'Invited Talks'), ('Editorial Boards', 'Editorial Boards')], default='Invited Talks', max_length=60),
        ),
        migrations.AlterField(
            model_name='team',
            name='category',
            field=models.CharField(choices=[('Team', 'Team'), ('Alumini', 'Alumini')], default='Team', max_length=60),
        ),
    ]
