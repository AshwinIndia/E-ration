from django.db import models

from django.db import models
from django.contrib.auth.models import User

class District(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tehsil(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.district.name}"

class FairPriceShop(models.Model):
    name = models.CharField(max_length=200)
    shop_number = models.CharField(max_length=50, unique=True)
    tehsil = models.ForeignKey(Tehsil, on_delete=models.CASCADE)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.shop_number})"

class RationCard(models.Model):
    CARD_TYPES = [
        ('APL', 'Above Poverty Line'),
        ('BPL', 'Below Poverty Line'),
        ('AAY', 'Antyodaya Anna Yojana'),
    ]
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=20, unique=True)
    card_type = models.CharField(max_length=3, choices=CARD_TYPES)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    fair_price_shop = models.ForeignKey(FairPriceShop, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.card_number} - {self.get_card_type_display()}"

class FamilyMember(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    ration_card = models.ForeignKey(RationCard, on_delete=models.CASCADE, related_name='family_members')
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    relationship = models.CharField(max_length=50)
    aadhar_number = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return f"{self.name} ({self.get_gender_display()})"

class Commodity(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=20)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.unit})"

class Entitlement(models.Model):
    card_type = models.CharField(max_length=3, choices=RationCard.CARD_TYPES)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.get_card_type_display()} - {self.commodity.name}"

class Distribution(models.Model):
    ration_card = models.ForeignKey(RationCard, on_delete=models.CASCADE)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    distribution_date = models.DateField()

    def __str__(self):
        return f"{self.ration_card.card_number} - {self.commodity.name} - {self.distribution_date}"

class Complaint(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
        ('CLOSED', 'Closed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ration_card = models.ForeignKey(RationCard, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Complaint {self.id} - {self.subject}"