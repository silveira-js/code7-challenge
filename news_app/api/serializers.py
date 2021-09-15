from rest_framework import serializers
from .models import Author, News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    news = NewsSerializer(read_only = True, many = True)
    class Meta:
        model = Author
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        author, _ = Author.objects.get_or_create(first_name=validated_data.get('first_name', None), 
                                                 last_name=validated_data.get('last_name', None))
        return author