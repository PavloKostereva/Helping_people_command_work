from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('donor', 'Благодійник'),
        ('seeker', 'Людина, якій потрібна допомога'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    
    groups = models.ManyToManyField(
        'auth.Group', related_name='custom_user_groups', blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='custom_user_permissions', blank=True
    )


class HelpRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Очікується'),
        ('in_progress', 'Виконується'),
        ('completed', 'Завершено'),
    ]
    seeker = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={'role': 'seeker'}
    )
    description = models.TextField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    qr_code = models.CharField(max_length=255, blank=True)

    def generate_qr_code(self):
        pass  # Логіка генерації QR-коду


class Donation(models.Model):
    STATUS_CHOICES = [
        ('accepted', 'Прийнято'),
        ('completed', 'Завершено'),
    ]
    donor = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={'role': 'donor'}
    )
    help_request = models.ForeignKey(HelpRequest, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='accepted')
    donation_date = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    route = models.CharField(max_length=255, blank=True)

    def complete_donation(self):
        self.status = 'completed'
        self.completed_at = models.DateTimeField(auto_now=True)
        self.save()


class Location(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    last_updated = models.DateTimeField(auto_now=True)


class Rating(models.Model):
    RATING_CHOICES = [
        (1, 'Погано'),
        (2, 'Середньо'),
        (3, 'Добре'),
    ]
    giver = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={'role': 'donor'}, related_name='given_ratings'
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={'role': 'seeker'}, related_name='received_ratings'
    )
    rating = models.IntegerField(choices=RATING_CHOICES)
    review = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Transaction(models.Model):
    donor = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={'role': 'donor'}
    )
    points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
