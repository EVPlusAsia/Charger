from rest_framework import serializers
import datetime
from .models import Article



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author']