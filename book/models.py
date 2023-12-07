from django.db import models
from django.utils import timezone


class City(models.Model):
    """
    Defines a city in database
    it used in Auhor model
    """
    CITY = (
        ('QOM', 'qom'),
        ('TEHRAN', 'tehran'),
        ('MASHHAD', 'mashhad')
    )
    def __str__(self):
        return self.CITY


class Author(models.Model):
    """
    Defines an Author in database 
    it used in Book model
    """
    AUTHOR_NAME = (
        ('william shakespeare', 'william shakespeare'),
        ('agatha christie', 'agatha christie'),
        ('barbara cartland', 'barbara cartland'),
        ('george orwell', 'george orwell')
    )
    author_name = models.CharField(choices=AUTHOR_NAME, default='shakespeare', max_length=255)
    author_city = models.CharField(choices=City.CITY, default='Qom', max_length=50)
    
    def __str__(self):
        return self.author_name


class Genre(models.Model):
    GENRE_CHOICE = (
        ('fantasy', 'Fantasy'),
        ('mystery', 'Mystery'),
        ('science fiction', 'Science fiction'),
        ('fiction', 'Fiction'),
        ('horror', 'Horror')
    )


class Book(models.Model):
    """Defines a book record in database"""

    name = models.CharField(max_length=350, null=False) 
    description = models.CharField(default='Description', max_length=1000)
    authors = models.ManyToManyField(Author, related_name='books')
    genre = models.CharField(choices=Genre.GENRE_CHOICE, default='Genre', max_length=50)
    publication_date = models.DateField(default=timezone.now)
    isbn = models.PositiveIntegerField(default=0000000000000)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=00.00)

    def __str__(self):
        return self.name
