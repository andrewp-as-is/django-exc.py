# Generated by Django 2.2.5 on 2019-10-02 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Traceback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField()),
                ('value', models.TextField()),
                ('traceback', models.TextField()),
                ('path', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'django_traceback',
                'ordering': ['-created_at'],
            },
        ),
    ]
