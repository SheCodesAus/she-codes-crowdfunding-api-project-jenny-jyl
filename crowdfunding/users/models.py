from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

# __str__ just turns user into text, which returns the username. Users all have username automatically and we simply inherit from it.