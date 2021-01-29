from django.db import models
from django.contrib.auth import get_user_model


class Payment(models.Model):
    stripe_id = models.CharField(max_length=50)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username