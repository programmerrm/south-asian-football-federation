from django import forms
from travel_claim.models import TravelClaim

# TRAVEL CLAIM FORM
class TravelClaimForm(forms.ModelForm):
    class Meta:
        model = TravelClaim
        fields = [
            "nature_of_duty",
            "event_name",
            "your_name",
            "designation",
            "nationality",
            "venue",
            "phone",
            "email",
            "departure_date",
            "return_date",
            "travelling_date",
            "travel_from",
            "travel_to",
            "ticket_cost",
            "amount_local_currency",
            "amount_usd",
            "exchange_rate",
            "number_of_days",
            "daily_calculation",
            "daily_total_usd",
            "incidental",
            "incidental_usd",
            "other_total_usd",
            "grand_total_usd",
            "attachment",
            "claimed_by",
            "date",
            "signature",
        ]
        widgets = {
            "departure_date": forms.DateInput(attrs={"type": "date"}),
            "return_date": forms.DateInput(attrs={"type": "date"}),
            "travelling_date": forms.DateInput(attrs={"type": "date"}),
            "date": forms.DateInput(attrs={"type": "date"}),
            "ticket_cost": forms.NumberInput(attrs={"step": "0.01"}),
            "amount_local_currency": forms.NumberInput(attrs={"step": "0.01"}),
            "amount_usd": forms.NumberInput(attrs={"step": "0.01"}),
            "exchange_rate": forms.NumberInput(attrs={"step": "0.0001"}),
            "daily_calculation": forms.NumberInput(attrs={"step": "0.01"}),
            "daily_total_usd": forms.NumberInput(attrs={"step": "0.01"}),
            "incidental": forms.NumberInput(attrs={"step": "0.01"}),
            "incidental_usd": forms.NumberInput(attrs={"step": "0.01"}),
            "other_total_usd": forms.NumberInput(attrs={"step": "0.01"}),
            "grand_total_usd": forms.NumberInput(attrs={"step": "0.01"}),
            "nature_of_duty": forms.RadioSelect
        }
        