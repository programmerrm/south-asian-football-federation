from django.urls import path
from travel_claim.views import TravelClaimView, TravelClaimSuccessView

urlpatterns = [
    path("travel-claim/", TravelClaimView.as_view(), name="travel_claim"),
    path("travel-claim/success/", TravelClaimSuccessView.as_view(), name="travel_claim_success"),
]
