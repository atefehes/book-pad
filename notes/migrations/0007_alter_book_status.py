# Generated by Django 4.1 on 2022-08-27 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_alter_book_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('0', 'not added'), ('1', 'added')], default='0', max_length=20),
        ),
    ]
