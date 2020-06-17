# Generated by Django 3.0.6 on 2020-05-28 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('keywords', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('company', models.CharField(max_length=150)),
                ('adress', models.CharField(blank=True, max_length=150)),
                ('phone', models.CharField(max_length=150)),
                ('fax', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('smtpserver', models.CharField(max_length=150)),
                ('smtpemail', models.CharField(max_length=150)),
                ('smtppassword', models.CharField(max_length=150)),
                ('smtpport', models.CharField(blank=True, max_length=5)),
                ('icon', models.ImageField(blank=True, upload_to='images/')),
                ('facebook', models.CharField(blank=True, max_length=150)),
                ('instagram', models.CharField(blank=True, max_length=150)),
                ('twitter', models.CharField(blank=True, max_length=150)),
                ('about', models.CharField(max_length=150)),
                ('references', models.TextField()),
                ('status', models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]