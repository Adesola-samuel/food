# Generated by Django 3.2.5 on 2021-10-22 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veriuser', '0002_alter_biodata_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biodata',
            name='department',
        ),
        migrations.RemoveField(
            model_name='biodata',
            name='matric_no',
        ),
        migrations.RemoveField(
            model_name='biodata',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='biodata',
            name='picture',
        ),
    ]
