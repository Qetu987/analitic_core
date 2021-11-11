from rest_framework import serializers
from .models import Heading


class HeadingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Heading
        fields = ('id', 'title', 'name_pattern')