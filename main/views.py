from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Heading
from .serializers import HeadingListSerializer


class HeadingListView(APIView):
    def get(delf, request):
        headings = Heading.objects.all()
        serializer = HeadingListSerializer(headings, many=True)
        return Response(serializer.data)