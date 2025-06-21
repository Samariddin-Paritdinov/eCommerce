from django.db.models import TextChoices


class OrderStatus(TextChoices):
    PENDING = 'PENDING', 'PENDING'
    IN_TRANSIT = 'IN_TRANSIT', 'IN_TRANSIT'
    DELIVERED = 'DELIVERED', 'DELIVERED'
    CANCELLED = 'CANCELLED', 'CANCELLED'