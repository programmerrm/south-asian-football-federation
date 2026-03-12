from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from configuration.models import Logo

# PORTAL VIEW SET
class PortalView(LoginRequiredMixin, TemplateView):
    template_name = 'portal/index.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Logo.objects.last()
        return context

