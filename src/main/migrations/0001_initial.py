# Generated by Django 3.2.9 on 2022-01-18 07:07

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import easy_thumbnails.fields
import main.utilities


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ABUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='Last name')),
                ('avatar', easy_thumbnails.fields.ThumbnailerImageField(default='avatars/default.png', upload_to=main.utilities.get_user_avatar_path, verbose_name='Avatar')),
                ('phone', models.CharField(blank=True, max_length=21, validators=[django.core.validators.RegexValidator(message='Wrong format!', regex='^(\\s*)?(\\+)?([- _():=+]?\\d[- _():=+]?){9,16}(\\s*)?$')], verbose_name='Phone')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Address')),
                ('location', django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(0.0, 0.0), srid=4326, verbose_name='Location')),
                ('about', models.TextField(blank=True, verbose_name='About')),
                ('experience', models.TextField(blank=True, verbose_name='Experience')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff status')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Superuser status')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last login')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ['email'],
            },
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_name', models.CharField(max_length=24, verbose_name='Name of icon')),
                ('link_url', models.URLField(verbose_name='URL of Link')),
                ('position', models.PositiveSmallIntegerField(db_index=True, verbose_name='Position')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Social Link',
                'verbose_name_plural': 'Social Links',
                'ordering': ['user', 'position'],
                'unique_together': {('user', 'position')},
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('progress', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Progress')),
                ('position', models.PositiveSmallIntegerField(db_index=True, verbose_name='Position')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
                'ordering': ['user', 'position'],
                'unique_together': {('user', 'position')},
            },
        ),
        migrations.CreateModel(
            name='ABUserTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('ru', 'Русский')], max_length=2, verbose_name='Language')),
                ('first_name', models.CharField(max_length=150, verbose_name='First name')),
                ('last_name', models.CharField(max_length=150, verbose_name='Last name')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('about', models.TextField(verbose_name='About')),
                ('experience', models.TextField(verbose_name='Experience')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'ABUser Translation',
                'verbose_name_plural': 'ABUser Translations',
                'ordering': ['user', 'language'],
                'unique_together': {('user', 'language')},
            },
        ),
    ]
