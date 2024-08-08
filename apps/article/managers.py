from django.db.models import Manager

from apps.article.choices import Status


class PublishManager(Manager):
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(status=Status.PUBLISHED)
