from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.


class LanguageTranslations(models.Model):
    objects = models.Manager()

    id = models.AutoField(primary_key=True, editable=False)

    translations = JSONField()

    class Meta:
        db_table = 'tbl__language_translations'
