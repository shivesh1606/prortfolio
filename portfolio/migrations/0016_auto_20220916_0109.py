# Generated by Django 2.2.9 on 2022-09-15 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_merge_20220916_0107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=3000)),
                ('url', models.CharField(max_length=3000)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('Journal', 'Journal'), ('Conference', 'Conference'), ('Articles', 'Articles'), ('International Reports', 'International Reports')], default='Journal', max_length=60),
        ),
    ]
