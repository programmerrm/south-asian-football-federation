from django.urls import path
from bank_account.views import BankAccountView

urlpatterns = [
    path("bank-account/", BankAccountView.as_view(), name="bank-account-view"),
]
