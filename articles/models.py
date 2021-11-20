from django.db import models


class Tag(models.Model):

    name = models.CharField(max_length=30, verbose_name='Название')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scopes = models.ManyToManyField(Tag, related_name='tags', through='Names_tags', through_fields=('article', 'tag'))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Names_tags(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='to_article')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='to_tag')
    main = models.BooleanField()

    def __str__(self):
        return '{0}_{1}'.format(self.article, self.tag)


