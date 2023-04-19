from rest_framework.generics import ListAPIView,GenericAPIView
from rest_framework.permissions import AllowAny
from Dashmed.language_fetcher.models import LanguageTranslations
from Dashmed.language_fetcher.seriailizers import LanguageTranslationsResponseSerializer
from rest_framework.response import Response


class TranslationsListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = LanguageTranslationsResponseSerializer
    queryset = LanguageTranslations.objects.all()


class TranslationsView(GenericAPIView):
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        return "lol"

    def get(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class()
        return Response(serializer.data)

