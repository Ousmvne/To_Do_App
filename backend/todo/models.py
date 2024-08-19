from django.db import models

# Create your models here.
class Todo(models.Model):
    DIFFICULTY_CHOICES = [
        ('Facile', 'Facile'),
        ('Moyen', 'Moyen'),
        ('Difficile', 'Difficile'),
    ]

    CATEGORY_CHOICES = [
        ('Personal', 'Personal'),
        ('Leisure', 'Leisure'),
        ('Work', 'Work'),
    ]

    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='Moyen')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='Personal')

    def __str__(self):
        return self.title
