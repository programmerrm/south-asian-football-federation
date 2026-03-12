from django.views.generic import FormView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
from accounts.forms import LoginForm
from configuration.models import Logo

# USER LOGIN VIEW SET
class LoginView(FormView):
    template_name = 'login/index.html'
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Logo.objects.last()
        return context

    def form_valid(self, form):
        username_or_email = form.cleaned_data["username_or_email"]
        password = form.cleaned_data["password"]

        user = authenticate(
            self.request,
            username=username_or_email,
            password=password
        )

        if user:
            login(self.request, user)
            messages.success(self.request, "Login successful")
            return redirect("portal-view")

        messages.error(self.request, "Invalid username/email or password")
        return self.form_invalid(form)
    