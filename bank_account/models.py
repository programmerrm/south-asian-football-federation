from django.db import models
from django.utils.translation import gettext_lazy as _

# BANK ACCOUNT
class BankAccount(models.Model):
    # SECTION A: APPLICANT DETAILS
    applicant_name = models.CharField(
        max_length=255,
        verbose_name=_("Applicant Name"),
        help_text=_("Full name of the applicant.")
    )
    country = models.CharField(
        max_length=255,
        verbose_name=_("Country"),
        help_text=_("Country of residence.")
    )
    email = models.EmailField(
        max_length=280,
        verbose_name=_("Email Address")
    )
    phone = models.CharField(
        max_length=20,
        verbose_name=_("Phone Number"),
        help_text=_("Contact number of applicant.")
    )
    # SECTION B: BANK DETAILS
    beneficiary_name = models.CharField(
        max_length=255,
        verbose_name=_("Name of Beneficiary")
    )
    bank_name = models.CharField(
        max_length=255,
        verbose_name=_("Bank Name")
    )
    bank_address = models.CharField(
        max_length=255,
        verbose_name=_("Bank Address Line 1")
    )
    account_number = models.CharField(
        max_length=100,
        verbose_name=_("Account Number")
    )
    iban_number = models.CharField(
        max_length=100,
        verbose_name=_("IBAN Number")
    )
    swift_code = models.CharField(
        max_length=50,
        verbose_name=_("SWIFT Code")
    )
    # CORRESPONDENT / INTERMEDIARY BANK
    correspondent_account_number = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_("Correspondent Bank Account Number")
    )
    correspondent_bank_address = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Correspondent Bank Address")
    )
    # DECLARATION
    declaration_name = models.CharField(
        max_length=255,
        verbose_name=_("Declaration Name"),
        help_text=_("Name written in declaration section.")
    )
    declaration_date = models.DateField(
        verbose_name=_("Declaration Date")
    )
    signature = models.CharField(
        max_length=255,
        verbose_name=_("Signature")
    )
    # SYSTEM FIELDS
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created At")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Last Updated")
    )
    # META
    class Meta:
        verbose_name = _("Bank Account Information")
        verbose_name_plural = _("Bank Account Informations")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.applicant_name} - {self.bank_name}"
    