# Generated by Django 3.2.6 on 2021-08-31 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empno', models.IntegerField()),
                ('ename', models.CharField(max_length=150)),
                ('salary', models.FloatField()),
            ],
        ),
    ]
