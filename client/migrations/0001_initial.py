# Generated by Django 2.0.1 on 2018-01-22 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ticker', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=2000)),
                ('release_date', models.DateTimeField(verbose_name='date published')),
                ('flashParent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='flash_children', to='client.Report')),
                ('previousReport', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='later_reports', to='client.Report')),
                ('sourceParent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='source_children', to='client.Report')),
            ],
        ),
        migrations.CreateModel(
            name='ReportCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary', models.BooleanField(default=True)),
                ('private', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Company')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Report')),
            ],
        ),
        migrations.CreateModel(
            name='ReportRelationshipType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='ReportStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='ReportType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.ReportStatus'),
        ),
        migrations.AddField(
            model_name='report',
            name='tickers',
            field=models.ManyToManyField(through='client.ReportCompany', to='client.Company'),
        ),
        migrations.AddField(
            model_name='report',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.ReportType'),
        ),
    ]
