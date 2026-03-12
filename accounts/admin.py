from django.contrib import admin
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.contrib.sessions.models import Session
from django.utils import timezone

from .models import User
from .forms import PasswordChangeForm

@admin.action(description="Change password for selected users")
def change_user_password(modeladmin, request, queryset):

    if "apply" in request.POST:
        form = PasswordChangeForm(request.POST)

        if form.is_valid():
            new_password = form.cleaned_data["new_password"]

            for user in queryset:
                user.password = make_password(new_password)
                user.save()

                send_mail(
                    "Your password has been changed",
                    f"Your new password is: {new_password}",
                    "admin@example.com",
                    [user.email],
                    fail_silently=True,
                )

            modeladmin.message_user(request, "Password updated successfully")
            return None

    else:
        form = PasswordChangeForm()

    return render(
        request,
        "admin/change_password.html",
        {
            "users": queryset,
            "form": form
        }
    )

@admin.action(description="Logout selected users")
def logout_users(modeladmin, request, queryset):
    sessions = Session.objects.filter(expire_date__gte=timezone.now())

    count = 0
    for session in sessions:
        data = session.get_decoded()
        user_id = data.get("_auth_user_id")
        if user_id and int(user_id) in queryset.values_list("id", flat=True):
            session.delete()
            count += 1

    modeladmin.message_user(request, f"{count} user(s) logged out successfully")

@admin.action(description="Logout all users")
def logout_all_users(modeladmin, request, queryset=None):
    Session.objects.all().delete()
    modeladmin.message_user(request, "All users have been logged out successfully")

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "username"]
    actions = [change_user_password, logout_users, logout_all_users]
    