from django.http import Http404
from rest_framework import generics, status
from .models import User, Product, ProductAccess, Lesson, ViewingHistory
from .serializers import UserSerializer, ProductSerializer, ProductAccessSerializer, LessonSerializer, ViewingHistorySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum
'''
Созданем заполнение для всех таблиц. ListCreateAPIView - позволяет просматривать(GET) и добавлять значения(POST)
для примера для всех таблиц создал json файлы
'''

class UserCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductAccessCreateView(generics.ListCreateAPIView):
    queryset = ProductAccess.objects.all()
    serializer_class = ProductAccessSerializer

class LessonCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class ViewingHistoryCreateView(generics.ListCreateAPIView):
    queryset = ViewingHistory.objects.all()
    serializer_class = ViewingHistorySerializer


'''
Реализовать API для выведения списка всех уроков 
по всем продуктам к которым пользователь имеет доступ, 
с выведением информации о статусе и времени просмотра.
'''

class HistoryAPIView(APIView):
    def get(self, request, user_id):
        history_entries = ViewingHistory.objects.filter(user_id=user_id)
        if history_entries.exists():
            serializer = ViewingHistorySerializer(history_entries, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            raise Http404("Записи просмотра не найдены для данного пользователя.")

'''
Реализовать API с выведением списка уроков по конкретному продукту
 к которому пользователь имеет доступ, 
 с выведением информации о статусе и времени просмотра, 
 а также датой последнего просмотра ролика.
'''
class ProductLessonAPIView(APIView):
    def get(self, request, user_id, product_id):
        try:
            # Проверяем, имеет ли пользователь доступ к продукту
            product = Product.objects.get(id=product_id, owner_id=user_id)

            # Получаем уроки, связанные с данным продуктом
            lessons = Lesson.objects.filter(products=product)

            # Получаем информацию о просмотре уроков этим пользователем
            viewing_history = ViewingHistory.objects.filter(user_id=user_id, lesson__in=lessons).order_by('view_time')

            # Сериализуем данные
            serializer = ViewingHistorySerializer(viewing_history, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Product.DoesNotExist:
            return Response("Продукт не найден или у пользователя нет доступа к данному продукту.", status=status.HTTP_404_NOT_FOUND)

'''
Реализовать API для отображения статистики по продуктам. 
Необходимо отобразить список всех продуктов на платформе, к каждому продукту приложить информацию:
    Количество просмотренных уроков от всех учеников.
    Сколько в сумме все ученики потратили времени на просмотр роликов.
    Количество учеников занимающихся на продукте.
    Процент приобретения продукта (рассчитывается исходя из 
    количества полученных доступов к продукту деленное на общее количество пользователей на платформе).

'''
class ProductStatsAPIView(APIView):
    '''
    lessons_viewed -Количество просмотренных уроков от всех учеников.
    total_view_time общее время потраченное на просмотр ролликов
    total_students - Количество учеников занимающихся на продукте
    purchase_percentage- Процент приобретения продукта
    '''
    def get(self, request):
        products = Product.objects.all()
        product_stats = []
        for product in products:
            lessons_viewed = ViewingHistory.objects.filter(lesson__products=product).count()
            total_view_time = \
            ViewingHistory.objects.filter(lesson__products=product).aggregate(total_view_time=Sum('view_time'))[
                'total_view_time']
            total_students = ProductAccess.objects.filter(product=product).count()
            total_users = User.objects.count()
            purchase_percentage = (total_students / total_users) * 100 if total_users > 0 else 0

            stats_data = {
                'product_id': product.id,
                'product_name': product.name,
                'total_lessons_viewed': lessons_viewed,
                'total_view_time': total_view_time,
                'total_students': total_students,
                'purchase_percentage': purchase_percentage,
            }
            product_stats.append(stats_data)

        return Response(product_stats)
