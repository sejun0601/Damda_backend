from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import Contact
from .serializers import ContactSerializer

import logging

logger = logging.getLogger(__name__)

class ContactCreateView(APIView):
    parser_classes = [MultiPartParser, FormParser]  # 파일 처리

    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)