from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# TRAVEL CLAIM FORM VIEW SET
class TravelClaimView(LoginRequiredMixin, TemplateView):
    template_name = 'travel_claim/index.html'
    login_url = '/'
