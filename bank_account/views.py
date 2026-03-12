from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# BANK ACCOUNT FORM VIEW SET
class BankAccountView(LoginRequiredMixin, TemplateView):
    template_name = 'bank_account/index.html'
    login_url = '/'
