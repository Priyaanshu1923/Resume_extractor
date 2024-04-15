from django.db import models

class Resume(models.Model):
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    text = models.TextField()

    def __str__(self):
        return self.email
