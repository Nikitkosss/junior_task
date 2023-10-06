from datetime import timedelta

from django.db.models import Prefetch
from myapp.models import Product
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User, UserLectures, UserProducts

from .serializers import UserProductSerializer


class StatisticsView(APIView):

    def get(self, request):
        result = []
        products_list = Product.objects.all().prefetch_related(
            'userproducts_set'
            ).prefetch_related('lesson_set__userlessoninfo_set')
        total_users = User.objects.all().count()

        for product in products_list:
            obj = {}
            obj['Id продукта'] = product.pk
            obj['Продукт'] = product.name
            obj[
                'Количество учеников на продукте'
                ] = product.userproducts_set.all().count()

            count = 0
            for lesson in product.lesson_set.all():
                for userlesson in lesson.userlessoninfo_set.all():
                    if userlesson.status == 'Просмотрено':
                        count += 1
            obj['Количество просмотренных уроков'] = count
            time_spent = timedelta()
            for lesson in product.lesson_set.all():
                for userlesson in lesson.userlessoninfo_set.all():
                    time_spent += userlesson.watched_time
            obj['Временя потраченное на просмотр роликов'] = time_spent

            obj['Процент приобретения продукта'] = (
                f"{product.userproducts_set.all().count() / total_users :.2%}"
            )
            result.append(obj)
        return Response(data=result, status=status.HTTP_200_OK)


class UserProductView(ListAPIView):
    queryset = UserProducts.objects.none()
    serializer_class = UserProductSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']

        userlesson = UserLectures.objects.filter(user__id=user_id)
        queryset = (
            UserProducts.objects.filter(
                user__id=user_id
                ).prefetch_related(
                    Prefetch(
                            'product__lesson_set__userlessoninfo_set',
                            queryset=userlesson))
            )
        return queryset


class UserProductDetailView(RetrieveAPIView):
    queryset = UserProducts.objects.none()
    serializer_class = UserProductSerializer

    def get_object(self):
        user_id = self.kwargs['user_id']
        product_id = self.kwargs['product_id']
        userlesson = UserLectures.objects.filter(user__id=user_id)
        obj = (
            UserProducts.objects.filter(
                user__id=user_id,
                product__id=product_id
                ).prefetch_related(
                    Prefetch('product__lesson_set__userlessoninfo_set',
                             queryset=userlesson))
            )
        if len(obj) == 0:
            raise ValidationError(detail={'detail': 'Incorrect product id'})
        return obj[0]
