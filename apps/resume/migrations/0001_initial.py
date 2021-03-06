# Generated by Django 3.2.4 on 2021-08-16 06:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChooseTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('theme', models.ImageField(blank=True, upload_to='theme/')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('objective', models.TextField(max_length=200)),
                ('date', models.DateTimeField(auto_now=True)),
                ('template', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.choosetemplate')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='WorkSamples',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=100)),
                ('project_link', models.CharField(max_length=100)),
                ('technology', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('responsibilities', models.TextField(max_length=1000)),
                ('logo', models.ImageField(upload_to='images/logos/')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.resume')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('skills', models.CharField(max_length=300)),
                ('date', models.DateTimeField(auto_now=True)),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.resume')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='ResumeUserDetails',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=100)),
                ('date_of_birth', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, default='../static/images/default_avatar.png', upload_to='')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('hobbies', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.resume')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=100)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('designation', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=1000)),
                ('place', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.resume')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('qualification_name', models.CharField(max_length=100)),
                ('year_of_passing', models.CharField(max_length=100)),
                ('percentage_or_grade', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.resume')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('certificate', models.CharField(max_length=300)),
                ('date_obtained', models.DateField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.resume')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('achievements', models.CharField(max_length=300)),
                ('date', models.DateTimeField(auto_now=True)),
                ('resume', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.resume')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
