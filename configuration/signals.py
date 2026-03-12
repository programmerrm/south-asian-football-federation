from django.db import models
from django.core.exceptions import ValidationError

# === BASE MODEL TO ALLOW ONLY ONE ROW IN DATABASE ====
class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def clean(self):
        model = self.__class__
        if not self.pk and model.objects.exists():
            raise ValidationError(f"Only one {model.__name__} instance is allowed.")

    def save(self, *args, **kwargs):
        self.full_clean()
