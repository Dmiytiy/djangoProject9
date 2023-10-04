
from django.db import models

# Create your models here.

class User(models.Model):
    '''
    Для отслеживания, какие пользователи просматривают уроки
    '''
    username = models.CharField(max_length=150, unique=True)
class Product(models.Model):
    '''
    Таблица Product:

    name - Поле для хранения названия продукта .
    owner - владелец. Внешний ключ для связи с пользователем-владельцем продукта
    '''
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ProductAccess(models.Model):
    ''''
    Для сохранения доступов к продукту для пользователей создадим модель ProductAccess
    product - внешний ключ для отслеживания к какому продукту есть доступ
    user - внешний ключ для отслеживания кому из пользователей есть доступ к продуктам
    '''
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"Access to {self.product.name}"


class Lesson(models.Model):
    '''
    Таблица "Урок":
    title - Поле для хранения названия урока
    video_url - Поле для хранения ссылки на видео .
    duration_seconds - Поле для хранения длительности просмотра
    products - Множественное поле для хранения продуктов, в которых находится урок
    '''
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    duration_seconds = models.IntegerField()
    products = models.ManyToManyField(Product)
    def __str__(self):
        return self.title
class ViewingHistory(models.Model):
    '''
    ViewingHistory - модель для отслеживания  просмотров уроков пользователями
    user и lesson, внешние ключи, связывающие просмотр с конкретным пользователем и уроком
    view_time - длительность просмотра в секундах
    STATUS_CHOICES - статус, содержит два кортежа: первый элемент - значение, которое будет сохранено в базе данных, и второй элемент - человекочитаемое описание этого значения
    status - поле должно принимать значения STATUS_CHOICES
    def save(self, *args, **kwargs) - функция для проверки, было ли просмотрено 80% ролика
    '''

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    view_time = models.PositiveIntegerField()
    STATUS_CHOICES = (
        ('П', 'Просмотрено'),
        ('Н', 'Не просмотрено'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def save(self, *args, **kwargs):
        # Проверяем, было ли просмотрено 80% ролика
        if self.view_time >= 0.8 * self.lesson.duration_seconds:
            self.status = 'П'
        else:
            self.status = 'Н'
        super().save(*args, **kwargs)