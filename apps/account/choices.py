from django.db.models import TextChoices


class AccountRole(TextChoices):
    CUSTOMER = 'customer', 'Customer'
    PUBLISHED = 'published', 'Published'
    WRITER = 'writer', 'Writer'
    MEMBER = 'member', 'Member'
