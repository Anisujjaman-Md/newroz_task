import random
from rest_framework import viewsets, pagination
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Quote
from .serializers import QuoteSerializer
from googletrans import Translator


class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    pagination_class = CustomPagination

    def retrieve(self, request, pk=None):
        try:
            quote = Quote.objects.get(pk=pk)
        except Quote.DoesNotExist:
            raise Http404("Quote does not exist")
        
        serializer = QuoteSerializer(quote)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if not queryset.exists():  
            return Response({"detail": "No quotes available."}, status=status.HTTP_404_NOT_FOUND)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def random(self, request):
        try:
            count = Quote.objects.count()
            random_index = random.randint(0, count - 1)
            random_quote = Quote.objects.all()[random_index]
        except IndexError:
            raise Http404("No quotes available.")
        
        serializer = QuoteSerializer(random_quote)
        return Response(serializer.data)


class BanglaQuoteViewSet(viewsets.ModelViewSet):
    serializer_class = QuoteSerializer

    def retrieve(self, request, pk=None):
        try:
            quote = Quote.objects.get(pk=pk)
        except Quote.DoesNotExist:
            return Response({"success": False, "message": "Quotes Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = QuoteSerializer(quote)

        translator = Translator()
        try:
            translated_quote = translator.translate(serializer.data['quote'], src='en', dest='bn').text
            translated_author = translator.translate(serializer.data['author'], src='en', dest='bn').text
        except Exception as e:
            return Response({"success": False, "message": "Error translating quote."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        response_data = {
            "success": False,
            "message": "Translated Quote Details",
            'quote': translated_quote,
            'author': translated_author,
        }
        return Response(response_data, status=status.HTTP_200_OK)
