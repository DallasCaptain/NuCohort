from django.db import models

class BookManager(models.Manager):

    def basic_validator(self, bookProps):
        errors={}
        if len(bookProps['title'])< 5:
            errors["title"] = "Book title should be at least 5 characters"
        if len(bookProps['description'])<10:
            errors['description'] = "Book description should be at least 10 characters"
        return errors

class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Authors(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField()
    books = models.ManyToManyField(Books, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
