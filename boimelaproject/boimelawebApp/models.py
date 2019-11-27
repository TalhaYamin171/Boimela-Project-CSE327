from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Stall(models.Model):
    BOOK = 'Book'
    FOOD = 'Food'
    STALL_TYPES = (
        (BOOK, 'Book'),
        (FOOD, 'Food'),
    )
    stall_name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    stall_type = models.CharField(max_length=10, choices=STALL_TYPES, default="Type N/A")

    class Meta:
        ordering = ('stall_name',)

    def __str__(self):
        return self.stall_name

    def get_absolute_url(self):
        return reverse('dashboard')


class Book(models.Model):
    SCIFI = 'SCIFI'
    ACTION = 'ACTION'
    HORROR = 'HORROR'
    ROMANTIC = 'ROMANTIC'
    NONFICTION = 'NONFICTION'
    FICTION = 'FICTION'
    CLASSIC = 'CLASSIC'
    POETRY = 'POETRY'
    THRILLER = 'THRILLER'
    MYSTERY = 'MYSTERY'
    CHILDREN = 'CHILDREN'

    BOOK_GENRES = (
        (SCIFI, 'SCI-FI'),
        (ACTION, 'ACTION'),
        (HORROR, 'HORROR'),
        (ROMANTIC, 'ROMANTIC'),
        (NONFICTION, 'NONFICTION'),
        (FICTION, 'FICTION'),
        (CLASSIC, 'CLASSIC'),
        (POETRY, 'POETRY'),
        (THRILLER, 'THRILLER'),
        (MYSTERY, 'MYSTERY'),
        (CHILDREN, 'CHILDREN'),
    )
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.IntegerField()
    book_genre = models.CharField(max_length=10, choices=BOOK_GENRES, default="Type N/A")
    release_date = models.DateField()
    stalls = models.ManyToManyField(Stall)

    class Meta:
        ordering = ('book_name',)

    def __str__(self):
        return self.book_name
