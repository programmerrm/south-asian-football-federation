from django import forms
from bank_account.models import BankAccount

# BANK ACCOUNT FORM
class BankAccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = [
            "applicant_name",
            "country",
            "email",
            "phone",
            "beneficiary_name",
            "bank_name",
            "bank_address",
            "account_number",
            "iban_number",
            "swift_code",
            "correspondent_account_number",
            "correspondent_bank_address",
            "declaration_name",
            "declaration_date",
            "signature",
        ]

        widgets = {
            "declaration_date": forms.DateInput(attrs={
                "type": "date"
            }),
        }
