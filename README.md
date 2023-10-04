# djangoProject9
Описание проекта 
Этот проект Django, с именем "djangoProject9", предоставляет API для образовательной платформы
создал таблицы согласно заданию
class User(models.Model):
    Для отслеживания, какие пользователи просматривают уроки

class Product(models.Model):
    '''
    Таблица Product:

    name - Поле для хранения названия продукта .
    owner - владелец. Внешний ключ для связи с пользователем-владельцем продукта
    '''
class ProductAccess(models.Model):
    ''''
    Для сохранения доступов к продукту для пользователей создадим модель ProductAccess
    product - внешний ключ для отслеживания к какому продукту есть доступ
    user - внешний ключ для отслеживания кому из пользователей есть доступ к продуктам
    '''
class Lesson(models.Model):
    '''
    Таблица "Урок":
    title - Поле для хранения названия урока
    video_url - Поле для хранения ссылки на видео .
    duration_seconds - Поле для хранения длительности просмотра
    products - Множественное поле для хранения продуктов, в которых находится урок
    '''
class ViewingHistory(models.Model):
    '''
    ViewingHistory - модель для отслеживания  просмотров уроков пользователями
    user и lesson, внешние ключи, связывающие просмотр с конкретным пользователем и уроком
    view_time - длительность просмотра в секундах
    STATUS_CHOICES - статус, содержит два кортежа: первый элемент - значение, которое будет сохранено в базе данных, и второй элемент - человекочитаемое описание этого значения
    status - поле должно принимать значения STATUS_CHOICES
    def save(self, *args, **kwargs) - функция для проверки, было ли просмотрено 80% ролика
    '''

Сериализаторы
UserSerializer: Сериализует экземпляры модели Пользователя.
ProductSerializer: Сериализует экземпляры модели Продукта.
ProductAccessSerializer: Сериализует экземпляры модели Доступа к Продукту.
LessonSerializer: Сериализует экземпляры модели Урока.
ViewingHistorySerializer: Сериализует экземпляры модели Истории Просмотров.

Views.py
UserCreateView: ListCreateAPIView для экземпляров модели Пользователя, позволяет отправлять GET и POST запросы.
ProductCreateView: ListCreateAPIView для экземпляров модели Продукта, позволяет отправлять GET и POST запросы.
ProductAccessCreateView: ListCreateAPIView для экземпляров модели Доступа к Продукту, позволяет отправлять GET и POST запросы.
LessonCreateView: ListCreateAPIView для экземпляров модели Урока, позволяет отправлять GET и POST запросы.
ViewingHistoryCreateView: ListCreateAPIView для экземпляров модели Истории Просмотров, позволяет отправлять GET и POST запросы.
HistoryAPIView: APIView для получения истории просмотров пользователя.
ProductLessonAPIView: APIView для получения уроков, связанных с определенным продуктом для пользователя.
ProductStatsAPIView: APIView для отображения статистики по продуктам, включая количество просмотренных уроков, общее время просмотра, количество студентов и процент покупок.

URL-адреса
/users/:  для создания и получения экземпляров Пользователя.
/products/:  для создания и получения экземпляров Продукта.
/product-access/:  для создания и получения экземпляров Доступа к Продукту.
/lessons/:  для создания и получения экземпляров Урока.
/viewing-history/:  для создания и получения экземпляров Истории Просмотров.
/api/<int:user_id>/:  для получения истории просмотров пользователя.
/api/users/<int:user_id>/<int:product_id>/: для получения уроков, связанных с определенным продуктом для пользователя.
/api/product_stats/:  для получения статистики по продуктам.
