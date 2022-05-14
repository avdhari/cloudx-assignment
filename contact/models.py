from django.db import models


class BaseModel(models.Model):
    is_removed = models.BooleanField(default=False)

    class Meta:
        abstract = True


class UserData(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name