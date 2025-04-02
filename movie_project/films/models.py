from django.db import models

# Create your models here.
class Film(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.CharField('Описание', max_length=500)
    review = models.CharField('Отзыв', max_length=300)

    # Выводит название фильма
    def __str__(self):
        return self.title


