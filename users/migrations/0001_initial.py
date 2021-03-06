# Generated by Django 3.0.1 on 2020-01-16 19:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('M', 'Mentor'), ('S', 'Startup')], default='S', max_length=1)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('EAD', 'Engineering & Data'), ('DESIGN', 'Design'), ('BUS', 'Business'), ('OTHER', 'other')], default='EAD', max_length=6)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
