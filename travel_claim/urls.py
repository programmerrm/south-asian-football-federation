from django.urls import path
from travel_claim.views import TravelClaimView

urlpatterns = [
    path("travel-claim/", TravelClaimView.as_view(), name="travel-claim-view"),
]
