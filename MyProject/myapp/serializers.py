from myapp.models import Lectures, Product
from rest_framework import serializers
from users.models import User, UserLectures, UserProducts


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'id']


class UserLecturesSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserLectures
        fields = ['id', 'status', 'watched_time', 'last_time_watched']


class LecturesSerializer(serializers.ModelSerializer):
    userlessoninfo_set = UserLecturesSerializer(many=True, read_only=True)

    class Meta:
        model = Lectures
        fields = [
            'id',
            'title',
            'video_link',
            'watchnig_time',
            'userlessoninfo_set'
        ]


class ProductSerializer(serializers.ModelSerializer):
    lesson_set = LecturesSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'owner', 'lesson_set']


class UserProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = UserProducts
        fields = ['user', 'product']
