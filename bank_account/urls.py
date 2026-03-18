from django.urls import path
from bank_account.views import BankAccountView, BankAccountSuccessView

urlpatterns = [
    path("bank-account/", BankAccountView.as_view(), name="bank_account"),
    path("bank-account/success/", BankAccountSuccessView.as_view(), name="bank_account_success"),
]