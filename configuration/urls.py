from django.urls import path
from configuration.views.login import LoginView
from configuration.views.portal import PortalView

urlpatterns = [
    path("", LoginView.as_view(), name="login-view"),
    path("portal/", PortalView.as_view(), name="portal-view"),
]
