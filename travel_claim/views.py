from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.views.generic import FormView, TemplateView
from travel_claim.forms import TravelClaimForm
from django.contrib.auth.mixins import LoginRequiredMixin

class TravelClaimView(LoginRequiredMixin, FormView):
    template_name = 'travel_claim/index.html'
    login_url = '/'
    form_class = TravelClaimForm
    success_url = reverse_lazy("travel_claim_success")

    def form_valid(self, form):
        # Store form data in session instead of saving immediately
        self.request.session["travel_claim_data"] = self.request.POST.dict()
        return redirect("travel_claim_success")

    def form_invalid(self, form):
        messages.error(self.request, "Form submission failed. Please check the fields.")
        return super().form_invalid(form)

# CONFIRMATION PAGE
class TravelClaimSuccessView(LoginRequiredMixin, TemplateView):
    template_name = "travel_claim/success.html"

    def get(self, request, *args, **kwargs):
        data = request.session.get("travel_claim_data")
        if not data:
            messages.error(request, "Please submit the form first.")
            return redirect("travel_claim")
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.session.get("travel_claim_data")
        if not data:
            return redirect("travel_claim")

        form = TravelClaimForm(data)
        if form.is_valid():
            travel_claim = form.save()

            # Admin email
            subject_admin = f"New Travel Claim Submitted: {travel_claim.nature_of_duty}"
            html_message_admin = render_to_string(
                "emails/admin_travel_claim.html",
                {"bank": travel_claim}  # Consider renaming "bank" to "claim" in template
            )
            email_admin = EmailMessage(
                subject_admin,
                html_message_admin,
                None,
                ["programmerwebrm@gmail.com"]
            )
            email_admin.content_subtype = "html"
            email_admin.send()

            # User email
            subject_user = "Thank you for submitting your travel claim"
            html_message_user = render_to_string(
                "emails/user_travel_claim.html",
                {"bank": travel_claim}  # Same note here about renaming context variable
            )
            email_user = EmailMessage(
                subject_user,
                html_message_user,
                None,
                [travel_claim.email]
            )
            email_user.content_subtype = "html"
            email_user.send()

            del request.session["travel_claim_data"]
            messages.success(request, "Travel claim saved successfully. Emails sent.")

        return redirect("travel_claim")
    