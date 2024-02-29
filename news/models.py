from django.db import models

class News(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(
        null=True, blank=True,
        upload_to='news_Image/'
    )
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Новости'

class AboutUs(models.Model):
    title = models.CharField(max_length=30)
    decs = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'страница "о нас"'


class Reviews(models.Model):
    title = models.CharField(max_length=50, verbose_name="ФИО")
    decs = models.TextField(verbose_name='Отзывы человека')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Отзывы'