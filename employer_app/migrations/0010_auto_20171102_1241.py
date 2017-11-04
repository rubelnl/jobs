# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-02 06:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employer_app', '0009_auto_20171102_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='age_range_form',
            field=models.IntegerField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='age_range_to',
            field=models.IntegerField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='category',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='jobpost_app.Category'),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='company',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='employer_app.Employer'),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='excl_job_flag',
            field=models.CharField(default='', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='exp_max',
            field=models.IntegerField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='exp_min',
            field=models.IntegerField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='exp_type',
            field=models.IntegerField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='gender',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='industry',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='jobpost_app.Industry'),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='job_level',
            field=models.IntegerField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='job_type',
            field=models.IntegerField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='last_date',
            field=models.DateTimeField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobpost_app.Location'),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='salary_max',
            field=models.IntegerField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='salary_min',
            field=models.IntegerField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='salary_range_type',
            field=models.IntegerField(default='', null=True),
        ),
    ]