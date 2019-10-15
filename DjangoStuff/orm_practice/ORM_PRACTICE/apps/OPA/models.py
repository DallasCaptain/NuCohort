from django.db import models

class User(models.Model):
    name = models.CharField(max_length=45)
    age = models.TextField()
    note = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Everthing works for Chris {self.name} ({self.age})>"