from django.db import models


class Specialist(models.Model):

    # Basic Information
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    video_consultation = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    suffix = models.JSONField(default=dict, null=True, blank=True)

    # Specialization & Professional Details
    practitioner = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    keyword_name = models.CharField(max_length=255, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    explanation = models.TextField(null=True, blank=True)
    connections_count = models.IntegerField(null=True, blank=True)
    created_at = models.CharField(max_length=500, null=True, blank=True)
    overall_experience = models.IntegerField(null=True, blank=True)
    reviews_total = models.IntegerField(null=True, blank=True)
    bedside_manner = models.IntegerField(null=True, blank=True)
    average_rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    registration_bodies = models.TextField(null=True, blank=True)
    last_review = models.JSONField(default=dict, null=True, blank=True)
    post_count = models.IntegerField(null=True, blank=True)
    hide_booking = models.BooleanField(default=False)
    plan = models.CharField(max_length=255, null=True, blank=True)
    connections = models.TextField(null=True, blank=True)
    updated_at = models.CharField(max_length=500, null=True, blank=True)

    # Multimedia & Media
    images = models.TextField(null=True, blank=True)
    statistic = models.TextField(null=True, blank=True)
    hide_appointment_request = models.BooleanField(default=False)
    basic = models.TextField(null=True, blank=True)
    years_as_specialist = models.CharField(max_length=500, null=True, blank=True)
    special_interests = models.TextField(null=True, blank=True)
    use_single_point_of_contact = models.BooleanField(default=False)

    # Contact Details
    phone = models.CharField(max_length=500, null=True, blank=True)
    email = models.CharField(max_length=500, null=True, blank=True)
    media = models.TextField(null=True, blank=True)
    demo = models.TextField(null=True, blank=True)
    secretary_name = models.CharField(max_length=255, null=True, blank=True)
    years_of_experience = models.CharField(max_length=255, null=True, blank=True)
    medical_procedures = models.TextField(null=True, blank=True)
    languages = models.CharField(max_length=500, null=True, blank=True)

    # Practice Details
    external_booking_link = models.URLField(max_length=500, null=True, blank=True)
    logo = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    working_opening_hours = models.TextField(null=True, blank=True)
    public_email_clarification_practice = models.CharField(max_length=500, null=True, blank=True)
    practice_type = models.CharField(max_length=500, null=True, blank=True)
    contact_details = models.TextField(null=True, blank=True)
    public_email_clarification = models.CharField(max_length=500, null=True, blank=True)
    reviews = models.TextField(null=True, blank=True)
    external_booking_link_practice = models.URLField(max_length=500, null=True, blank=True)
    is_public_system = models.BooleanField(default=False)
    consultation_fees = models.JSONField(default=dict, null=True, blank=True)
    peer_recommendations_count = models.IntegerField(null=True, blank=True)
    patients_children = models.BooleanField(default=False)
    hide_call = models.BooleanField(default=False)
    customer = models.TextField(null=True, blank=True)
    score = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    statistic_length = models.IntegerField(null=True, blank=True)
    education = models.TextField(null=True, blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
