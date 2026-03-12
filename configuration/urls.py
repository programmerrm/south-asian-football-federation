from django.urls import path
from configuration.views.portal import PortalView
from configuration.views.login import LoginView

urlpatterns = [
    path("portal/", PortalView.as_view(), name="portal-view"),
    path("", LoginView.as_view(), name="login-view"),
]
