from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Object(models.Model):
    obj = models.CharField(max_length=256, verbose_name='Объект')
    chain = models.ManyToManyField(Article, through='Membership')


class Relationship(models.Model):
    chain = models.ManyToManyField(Article)
