from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.views.generic import FormView, TemplateView
from bank_account.forms import BankAccountForm
from django.contrib.auth.mixins import LoginRequiredMixin

class BankAccountView(LoginRequiredMixin, FormView):
    template_name = "bank_account/index.html"
    form_class = BankAccountForm
    login_url = "/"
    success_url = reverse_lazy("bank_account_success")

    def form_valid(self, form):
        self.request.session["bank_form_data"] = self.request.POST.dict()

        return redirect("bank_account_success")

    def form_invalid(self, form):
        messages.error(self.request, "Form submission failed. Please check the fields.")
        return super().form_invalid(form)

# CONFIRMATION PAGE
class BankAccountSuccessView(LoginRequiredMixin, TemplateView):
    template_name = "bank_account/success.html"

    def get(self, request, *args, **kwargs):
        data = request.session.get("bank_form_data")

        if not data:
            messages.error(request, "Please submit the form first.")
            return redirect("bank_account")

        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        data = request.session.get("bank_form_data")

        if not data:
            return redirect("bank_account")

        form = BankAccountForm(data)

        if form.is_valid():

            bank_account = form.save()

            subject_admin = f"New Bank Account Submitted: {bank_account.applicant_name}"

            html_message_admin = render_to_string(
                "emails/admin_bank_account.html",
                {"bank": bank_account}
            )

            email_admin = EmailMessage(
                subject_admin,
                html_message_admin,
                None,
                ["programmerwebrm@gmail.com"]
            )

            email_admin.content_subtype = "html"
            email_admin.send()

            subject_user = "Thank you for submitting your bank details"

            html_message_user = render_to_string(
                "emails/user_bank_account.html",
                {"bank": bank_account}
            )

            email_user = EmailMessage(
                subject_user,
                html_message_user,
                None,
                [bank_account.email]
            )

            email_user.content_subtype = "html"
            email_user.send()

            del request.session["bank_form_data"]

            messages.success(request, "Bank account saved successfully.")

        return redirect("bank_account")
    