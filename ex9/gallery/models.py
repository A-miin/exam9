from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings

class Album(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(max_length=1024, null=True, blank=True, verbose_name='Описание')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="albums")
    created_at = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=False, verbose_name='Приватность')
    favorite = models.ManyToManyField(get_user_model(), related_name="favorite_albums", verbose_name='Избранные альбомы', blank=True)

    class Meta:
        db_table = 'albums'
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        return f'{self.name}: {self.description}'

class Photo(models.Model):
    photo = models.ImageField(upload_to='pics', verbose_name="Фотография")
    title = models.CharField(max_length=256, verbose_name="Подпись")
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="photos")
    album = models.ForeignKey('gallery.Album', on_delete=models.CASCADE,related_name="photos", null = True, blank = True)
    is_private = models.BooleanField(default=False, verbose_name='Приватность')
    favorite = models.ManyToManyField(get_user_model(), related_name="favorite_photos", verbose_name='Избранные фото', blank=True)

    class Meta:
        db_table = 'photos'
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f'{self.author}:{self.title}'

    # def has_link(self):
    #     if self.link.exists():
    #         return True
    #     else:
    #         return False


class Link(models.Model):
    photo = models.OneToOneField('gallery.Photo', on_delete=models.CASCADE, related_name='link')
    link = models.CharField(max_length=512)
    class Meta:
        verbose_name='Link'
        verbose_name_plural='Links'
    def __str__(self):
        return f'{self.link}'