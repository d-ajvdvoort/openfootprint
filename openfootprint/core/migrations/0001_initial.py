# Generated by Django 2.2.1 on 2019-06-07 23:58

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('source_name', models.CharField(db_index=True, max_length=250, verbose_name='Name')),
                ('source_country', models.CharField(blank=True, db_index=True, max_length=2, verbose_name='Country')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Latitude')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Longitude')),
                ('country', models.CharField(blank=True, max_length=2, null=True, verbose_name='Country')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('area', models.FloatField(blank=True, null=True)),
                ('is_default', models.BooleanField(default=False)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='core.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('kind', models.CharField(choices=[('employee', 'Employee'), ('attendee', 'Attendee'), ('other', 'Other')], default='other', max_length=30)),
                ('home_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Address')),
                ('main_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='people', to='core.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=100, populate_from='name', unique=True, verbose_name='Slug')),
                ('kind', models.CharField(choices=[('company', 'Company'), ('event', 'Event'), ('household', 'Household')], default='company', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='core.Project')),
            ],
        ),
        migrations.CreateModel(
            name='TransportMode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='TransportStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('from_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='core.Address')),
                ('mode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.TransportMode')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transportsteps', to='core.Project')),
                ('to_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='core.Address')),
                ('transport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transportsteps', to='core.TransportMode')),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='Name')),
                ('roundtrip', models.BooleanField(default=True)),
                ('frequency', models.CharField(choices=[('none', 'N times'), ('workday', 'Every work day'), ('perweek', 'N per week'), ('permonth', 'N per month'), ('peryear', 'N per year')], default='none', max_length=30)),
                ('frequency_n', models.IntegerField(default=1)),
                ('weight', models.FloatField(default=1.0)),
                ('done_at', models.DateTimeField(blank=True, null=True)),
                ('return_at', models.DateTimeField(blank=True, null=True)),
                ('from_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='core.Address')),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Person')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transports', to='core.Project')),
                ('tags', models.ManyToManyField(blank=True, to='core.Tag')),
                ('to_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='core.Address')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='people', to='core.Project'),
        ),
        migrations.AddField(
            model_name='person',
            name='tags',
            field=models.ManyToManyField(blank=True, to='core.Tag'),
        ),
        migrations.AddField(
            model_name='location',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='core.Project'),
        ),
        migrations.AddField(
            model_name='location',
            name='tags',
            field=models.ManyToManyField(blank=True, to='core.Tag'),
        ),
        migrations.CreateModel(
            name='Footprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('version', models.CharField(max_length=50, verbose_name='CR version')),
                ('footprint', models.FloatField(blank=True, null=True, verbose_name='Footprint in gCO2e')),
                ('raw_json', models.TextField(verbose_name='Raw JSON')),
                ('starts_at', models.DateTimeField(blank=True, null=True)),
                ('ends_at', models.DateTimeField(blank=True, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='footprints', to='core.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('kind', models.CharField(choices=[('co2e', 'Raw CO2e in g'), ('wh', 'Watt hours')], default='co2e', max_length=30)),
                ('param_f1', models.FloatField(blank=True, null=True)),
                ('param_f2', models.FloatField(blank=True, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extras', to='core.Project')),
                ('tags', models.ManyToManyField(blank=True, to='core.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('wh', models.FloatField()),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='core.Location')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='powerdatapoints', to='core.Project')),
            ],
        ),
    ]
