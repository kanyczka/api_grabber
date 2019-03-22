from django.contrib.auth.models import User
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from api.serializers import UserSerializer, UrlTextSerializer
from .models import UrlText
import datetime
import requests
from bs4 import BeautifulSoup


def get_text(markup_data):
    soup = BeautifulSoup(markup_data, 'lxml')
    for s in soup(['script', 'style']):
        s.decompose()
    return ' '.join(soup.stripped_strings)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class UrlTextViewSet(viewsets.ModelViewSet):
    serializer_class = UrlTextSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=url_path', '=text')

    def get_queryset(self):
        url_path = self.request.query_params.get('url_path', None)
        if url_path:
            url_texts = UrlText.objects.filter(url_path__icontains=url_path)
        else:
            url_texts = UrlText.objects.all()
        return url_texts

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UrlTextSerializer(instance)
        return Response(serializer.data)


    # tworzy rekord z adresem podanej strony, z tekstem ściągniętym z tej strony i z datą i czasem zapisu
    def create(self, request, *args, **kwargs):
        url_path = request.data['url_path']
        response = requests.get(url_path)
        if response:
            url_data = response.text
            text = get_text(url_data)
            url_text = UrlText.objects.create(url_path=url_path, text=text, upload_date=datetime.datetime.now())
            serializer = UrlTextSerializer(url_text, many=False)
            return Response(serializer.data)
        else:
            return Response (f"Server error, status code: {response.status_code}")

    def destroy(self, request, *args, **kwargs):
        url_text = self.get_object()
        url_text.delete()
        return Response("Text deleted")

    # metoda /delete_text - usuwa wybrany rekord
    @action(detail=True)
    def delete_text(self, request, **kwargs):
        url_text = self.get_object()
        url_text.delete()
        return Response("Deleted")

    # metoda /update_all - aktualizauje tekst z każdego adresu strony zapisanego w bazie danych
    @action(detail=False, methods=['post'])
    def update_all(self, reqest, **kwargs):
        url_texts = UrlText.objects.all()
        bad_response = 0
        ok_response = 0
        for url_text in url_texts:
            response = requests.get(url_text.url_path)
            if response:
                url_data = response.text
                url_text.text = get_text(url_data)
                url_text.upload_date = datetime.datetime.now()
                url_text.save()
                ok_response += 1
            else:
                bad_response +=1
                pass
        # serializer = UrlTextSerializer(url_texts, many=True)
        return Response(f'Updated: {ok_response}, Not updated: {bad_response}')








    # def perform_create(self, serializer):
    #     serializer.save()
    #
    # def get_success_headers(self, data):
    #     try:
    #         return {'Location': str(data[api_settings.URL_FIELD_NAME])}
    #     except (TypeError, KeyError):
    #         return {}

