# Generated by Django 2.1.14 on 2019-12-01 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0019_auto_20191201_1426'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='annotationtag',
            options={'ordering': ['sortkey', 'key']},
        ),
        migrations.AlterModelOptions(
            name='objecttype',
            options={'ordering': ['sortkey', 'key']},
        ),
        migrations.AlterModelOptions(
            name='subobjecttype',
            options={'ordering': ['sortkey', 'key']},
        ),
        migrations.AddField(
            model_name='subobjecttype',
            name='is_text_annotation',
            field=models.BooleanField(default=False),
        ),
    ]