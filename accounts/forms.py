from django import forms

# LOGIN FROM
class LoginForm(forms.Form):
    username_or_email = forms.CharField(
        label="Username or Email",
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": "w-full mt-1 mb-4 px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-400",
            "placeholder": "Username or Email"
        })
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "class": "w-full pl-3 pr-6 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-400 password-input",
            "placeholder": "Password"
        })
    )

    def __init__(self, *args, **kwargs):
        label_class = kwargs.pop("label_class", "block text-sm font-medium text-gray-700")
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.label_suffix = ""
            field.widget.attrs.update({"aria-label": field.label})
            field.label_class = label_class

# ADMIN ALL USER PASSWORD CHANGE 
class PasswordChangeForm(forms.Form):
    new_password = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput
    )
    