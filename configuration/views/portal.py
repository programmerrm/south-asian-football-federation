from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# PORTAL VIEW SET
class PortalView(LoginRequiredMixin, TemplateView):
    template_name = 'portal/index.html'
    login_url = '/'
