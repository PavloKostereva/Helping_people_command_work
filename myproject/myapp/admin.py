from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, HelpRequest, Donation, Location, Rating, Transaction

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'role', 'email_verified', 'phone_verified', 'points_balance')
    list_filter = ('role', 'email_verified', 'phone_verified')
    fieldsets = UserAdmin.fieldsets + (  # кастомні поля
        ('Додаткові дані', {'fields': ('role', 'email_verified', 'phone_verified', 'points_balance')}),
    )

@admin.register(HelpRequest)
class HelpRequestAdmin(admin.ModelAdmin):
    list_display = ('seeker', 'description', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('description', 'seeker__username')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('donor', 'help_request', 'status', 'donation_date', 'completed_at')
    list_filter = ('status',)
    search_fields = ('donor__username', 'help_request__description')
    readonly_fields = ('donation_date', 'completed_at')

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'latitude', 'longitude', 'last_updated')
    search_fields = ('user__username',)
    readonly_fields = ('last_updated',)

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('giver', 'receiver', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('giver__username', 'receiver__username')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('donor', 'points', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('donor__username',)
    readonly_fields = ('created_at',)






#реєстрація кастомного користувача
admin.site.register(User, CustomUserAdmin)
