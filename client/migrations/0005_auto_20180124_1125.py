# Generated by Django 2.0.1 on 2018-01-24 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20180124_1026'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reportrenderingstrategy',
            options={'verbose_name_plural': 'Report Rendering Strategies'},
        ),
        migrations.AlterModelOptions(
            name='reportstatus',
            options={'verbose_name_plural': 'Report Statuses'},
        ),
        migrations.RemoveField(
            model_name='report',
            name='private',
        ),
        migrations.AlterField(
            model_name='report',
            name='previousReport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='later_reports', to='client.Report'),
        ),
        migrations.AlterField(
            model_name='report',
            name='product_line',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to='client.ProductLine'),
        ),
        migrations.AlterField(
            model_name='report',
            name='rendering_strategy',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to='client.ReportRenderingStrategy'),
        ),
        migrations.AlterField(
            model_name='report',
            name='sourceParent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='source_children', to='client.Report'),
        ),
    ]
