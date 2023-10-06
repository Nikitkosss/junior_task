from django.contrib.auth import get_user_model
from django.db import models
from myapp.models import Lectures, Product

User = get_user_model()


class UserProducts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ['user', 'product']

    def __str__(self) -> str:
        return f"{self.user.username}"


class UserLectures(models.Model):

    watched_time = models.DurationField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lectures = models.ForeignKey(Lectures, on_delete=models.CASCADE)
    status = models.CharField()
    last_time_watched = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.watched_time >= self.lectures.watchnig_time * 0.8:
            self.status = 'Просмотрено'
        else:
            self.status = 'Не просмотрено'
        return super().save(*args, **kwargs)

    class Meta:
        unique_together = ['user', 'lectures']

    def __str__(self) -> str:
        return f"pk-{self.pk}"
