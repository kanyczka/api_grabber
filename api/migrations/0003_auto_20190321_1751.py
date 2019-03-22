# Generated by Django 2.1.7 on 2019-03-21 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190321_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=256)),
                ('text', models.TextField(blank=True)),
                ('upload_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Category')),
                ('site_text', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.SiteText')),
            ],
            options={
                'ordering': ['url', 'category'],
            },
        ),
        migrations.RemoveField(
            model_name='urltext',
            name='category',
        ),
        migrations.DeleteModel(
            name='URLText',
        ),
    ]
