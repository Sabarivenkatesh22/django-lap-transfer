import random
import string
from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    description = models.TextField()
    genre = models.CharField(max_length=50)
    

    def generate_isbn():
        while True:
            # Generate a random ISBN
            isbn = '978' + ''.join(random.choices(string.digits, k=9))
            
            # Check if the generated ISBN already exists in the database
            if not Book.objects.filter(ISBN=isbn).exists():
                return isbn

    # Add other fields as needed
    ISBN = models.CharField(max_length=13, unique=True, default=generate_isbn)

    class meta:
        verbose_name = "Book"
