from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
# Changes the name from the default model in admin db panel so names inputted can be seen
    def __str__(self):
        return self.name