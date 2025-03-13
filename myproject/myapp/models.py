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

class HelpRequest(models.Model):
    seeker = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'seeker'})
    description = models.TextField()
    location = models.CharField(max_length=255)  # Можна зберігати адресу або координати
    status = models.CharField(max_length=10, choices=[('pending', 'Очікується'), ('in_progress', 'Виконується'), ('completed', 'Завершено')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    qr_code = models.CharField(max_length=255, blank=True)  # Зберігаємо QR-код

    def generate_qr_code(self):
        # функціоналдля генерації
        pass
class Donation(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'donor'})
    help_request = models.ForeignKey(HelpRequest, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('accepted', 'Прийнято'), ('completed', 'Завершено')])
    donation_date = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    route = models.CharField(max_length=255, blank=True)  # Можна зберігати маршрут

    def complete_donation(self):
        # Функція для завершення допомоги
        pass



class Location(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    last_updated = models.DateTimeField(auto_now=True)



class Rating(models.Model):
    giver = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'donor'})
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'seeker'})
    rating = models.IntegerField(choices=[(1, 'Погано'), (2, 'Середньо'), (3, 'Добре')])
    review = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)



class Transaction(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'donor'})
    points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
