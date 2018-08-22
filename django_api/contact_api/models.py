from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    last_edited_by = models.CharField(max_length=50, default='sarahkirk')

    def __str__(self):
        return self.full_name
