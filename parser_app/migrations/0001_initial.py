# Generated by Django 5.1.3 on 2024-11-22 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
                ('video_consultation', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('suffix', models.JSONField(blank=True, default=dict, null=True)),
                ('practitioner', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('keyword_name', models.CharField(blank=True, max_length=255, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('explanation', models.TextField(blank=True, null=True)),
                ('connections_count', models.IntegerField(blank=True, null=True)),
                ('created_at', models.CharField(blank=True, max_length=500, null=True)),
                ('overall_experience', models.IntegerField(blank=True, null=True)),
                ('reviews_total', models.IntegerField(blank=True, null=True)),
                ('bedside_manner', models.IntegerField(blank=True, null=True)),
                ('average_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('registration_bodies', models.TextField(blank=True, null=True)),
                ('last_review', models.JSONField(blank=True, default=dict, null=True)),
                ('post_count', models.IntegerField(blank=True, null=True)),
                ('hide_booking', models.BooleanField(default=False)),
                ('plan', models.CharField(blank=True, max_length=255, null=True)),
                ('connections', models.TextField(blank=True, null=True)),
                ('updated_at', models.CharField(blank=True, max_length=500, null=True)),
                ('images', models.TextField(blank=True, null=True)),
                ('statistic', models.TextField(blank=True, null=True)),
                ('hide_appointment_request', models.BooleanField(default=False)),
                ('basic', models.TextField(blank=True, null=True)),
                ('years_as_specialist', models.CharField(blank=True, max_length=500, null=True)),
                ('special_interests', models.TextField(blank=True, null=True)),
                ('use_single_point_of_contact', models.BooleanField(default=False)),
                ('phone', models.CharField(blank=True, max_length=500, null=True)),
                ('email', models.CharField(blank=True, max_length=500, null=True)),
                ('media', models.TextField(blank=True, null=True)),
                ('demo', models.TextField(blank=True, null=True)),
                ('secretary_name', models.CharField(blank=True, max_length=255, null=True)),
                ('years_of_experience', models.CharField(blank=True, max_length=255, null=True)),
                ('medical_procedures', models.TextField(blank=True, null=True)),
                ('languages', models.CharField(blank=True, max_length=500, null=True)),
                ('external_booking_link', models.URLField(blank=True, max_length=500, null=True)),
                ('logo', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('working_opening_hours', models.TextField(blank=True, null=True)),
                ('public_email_clarification_practice', models.CharField(blank=True, max_length=500, null=True)),
                ('practice_type', models.CharField(blank=True, max_length=500, null=True)),
                ('contact_details', models.TextField(blank=True, null=True)),
                ('public_email_clarification', models.CharField(blank=True, max_length=500, null=True)),
                ('reviews', models.TextField(blank=True, null=True)),
                ('external_booking_link_practice', models.URLField(blank=True, max_length=500, null=True)),
                ('is_public_system', models.BooleanField(default=False)),
                ('consultation_fees', models.JSONField(blank=True, default=dict, null=True)),
                ('peer_recommendations_count', models.IntegerField(blank=True, null=True)),
                ('patients_children', models.BooleanField(default=False)),
                ('hide_call', models.BooleanField(default=False)),
                ('customer', models.TextField(blank=True, null=True)),
                ('score', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('statistic_length', models.IntegerField(blank=True, null=True)),
                ('education', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
