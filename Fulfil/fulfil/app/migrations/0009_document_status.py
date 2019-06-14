# Generated by Django 2.2.2 on 2019-06-14 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_document_elements'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='status',
            field=models.CharField(choices=[('COMPLETED', 'Completed'), ('INPROGRESS', 'In Progress')], default='INPROGRESS', max_length=20),
        ),
    ]