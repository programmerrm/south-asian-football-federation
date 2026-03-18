from django.db import models
from django.utils.translation import gettext_lazy as _

# TRAVEL CLAIM
class TravelClaim(models.Model):
    # NATURE OF DUTY 
    class DutyType(models.TextChoices):
        TOURNAMENT = "TOURNAMENT", _("Tournament")
        SEMINAR = "SEMINAR", _("Seminar")
        EVENT = "EVENT", _("Event")
        OTHERS = "OTHERS", _("Others")

    nature_of_duty = models.CharField(
        max_length=20,
        choices=DutyType.choices,
        verbose_name=_("Nature of Duty"),
        help_text=_("Select the purpose of travel.")
    )
    # BASIC INFORMATION
    event_name = models.CharField(
        max_length=255,
        verbose_name=_("Event Name"),
        help_text=_("Name of the tournament, seminar or event.")
    )
    your_name = models.CharField(
        max_length=255,
        verbose_name=_("Your Full Name")
    )
    designation = models.CharField(
        max_length=255,
        verbose_name=_("Designation / Position")
    )
    nationality = models.CharField(
        max_length=100,
        verbose_name=_("Nationality")
    )
    venue = models.CharField(
        max_length=255,
        verbose_name=_("Venue"),
        help_text=_("Location where the event was held.")
    )
    phone = models.CharField(
        max_length=20,
        verbose_name=_("Phone Number")
    )
    email = models.EmailField(
        max_length=280,
        verbose_name=_("Email Address")
    )
    # TRIP DURATION
    departure_date = models.DateField(
        verbose_name=_("Departure Date")
    )
    return_date = models.DateField(
        verbose_name=_("Return Date")
    )
    # TRAVELLING EXPENSES
    travelling_date = models.DateField(
        verbose_name=_("Travelling Date")
    )
    travel_from = models.CharField(
        max_length=255,
        verbose_name=_("Travel From")
    )
    travel_to = models.CharField(
        max_length=255,
        verbose_name=_("Travel To")
    )
    ticket_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Ticket Cost"),
        help_text=_("Airfare ticket cost in local currency.")
    )
    amount_local_currency = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=_("Amount in Local Currency")
    )
    amount_usd = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=_("Amount in USD")
    )
    exchange_rate = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        verbose_name=_("Exchange Rate"),
        help_text=_("1 USD equals how much local currency.")
    )
    # DAILY ALLOWANCE
    number_of_days = models.PositiveIntegerField(
        verbose_name=_("Number of Days")
    )
    daily_calculation = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=_("Daily Allowance (Per Day USD)")
    )
    daily_total_usd = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=_("Total Daily Allowance (USD)")
    )
    # OTHER EXPENSES
    incidental = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Incidental Expense 1 Description")
    )
    incidental_usd = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name=_("Incidental Expense 1 (USD)")
    )
    other_total_usd = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name=_("Other Expenses Total (USD)")
    )
    # GRAND TOTAL
    grand_total_usd = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name=_("Grand Total (USD)")
    )
    # FILE UPLOAD
    attachment = models.FileField(
        upload_to="travel_claims/",
        blank=True,
        null=True,
        verbose_name=_("Attachment"),
        help_text=_("Upload supporting documents (tickets, receipts etc.).")
    )
    # CLAIM INFO
    claimed_by = models.CharField(
        max_length=255,
        verbose_name=_("Claimed By")
    )
    date = models.DateField(
        verbose_name=_("Date")
    )
    signature = models.CharField(
        max_length=280,
        verbose_name=_('Signature'),
    )
    # META
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created At")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Last Updated")
    )

    class Meta:
        verbose_name = _("Travel Claim")
        verbose_name_plural = _("Travel Claims")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.your_name} - {self.event_name}"
    