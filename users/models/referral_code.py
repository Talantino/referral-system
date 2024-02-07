from django.db import models


class ReferralCode(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    expiry_date = models.DateField()
    code = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
