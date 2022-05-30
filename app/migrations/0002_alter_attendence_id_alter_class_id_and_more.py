# Generated by Django 4.0.4 on 2022-05-24 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='class',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='classattendence',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='excelfileupload',
            name='file',
            field=models.FileField(upload_to='../static/excel'),
        ),
        migrations.AlterField(
            model_name='excelfileupload',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='SubjectAttendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentroll', models.IntegerField()),
                ('att_count', models.IntegerField(default=0)),
                ('classname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.class')),
                ('subjectname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.subject')),
            ],
        ),
    ]
