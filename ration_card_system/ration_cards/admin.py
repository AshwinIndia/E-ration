from django.contrib import admin
from .models import District, Tehsil, FairPriceShop, RationCard, FamilyMember, Commodity, Entitlement, Distribution, Complaint

@admin.register(RationCard)
class RationCardAdmin(admin.ModelAdmin):
    list_display = ('card_number', 'user', 'card_type', 'status', 'issue_date', 'expiry_date', 'fair_price_shop')
    list_filter = ('status', 'card_type', 'issue_date', 'expiry_date')
    search_fields = ('card_number', 'user__username', 'fair_price_shop__name')

    actions = ['approve_ration_cards', 'reject_ration_cards']

    def approve_ration_cards(self, request, queryset):
        queryset.update(status='APPROVED')
        self.message_user(request, f"{queryset.count()} ration cards have been approved.")
    approve_ration_cards.short_description = "Approve selected ration cards"

    def reject_ration_cards(self, request, queryset):
        queryset.update(status='REJECTED')
        self.message_user(request, f"{queryset.count()} ration cards have been rejected.")
    reject_ration_cards.short_description = "Reject selected ration cards"

# Register the other models
admin.site.register(District)
admin.site.register(Tehsil)
admin.site.register(FairPriceShop)
admin.site.register(FamilyMember)
admin.site.register(Commodity)
admin.site.register(Entitlement)
admin.site.register(Distribution)
admin.site.register(Complaint)
