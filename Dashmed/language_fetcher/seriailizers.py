from rest_framework import serializers
from Dashmed.language_fetcher.models import LanguageTranslations


class LanguageTranslationsResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageTranslations
        fields = '__all__'
