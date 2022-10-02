from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from uuid import uuid4


class Category(models.Model):
    title = models.CharField(max_length=255)
    service_type = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return self.title


class ProductAndService(models.Model):
    name = models.CharField(max_length=255)
    unit_price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')

    def __str__(self) -> str:
        return self.name


class Customer(models.Model):

    phone_number = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'

    def first_name(self):
        return f'{self.user.first_name}'

    def last_name(self):
        return f'{self.user.last_name}'


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return str(self.id)


class Reception(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, related_name='cart_id')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    entry_date = models.DateField()
    total_price = models.IntegerField()
    payment_status = models.CharField(
        max_length=1,
        choices=PAYMENT_STATUS_CHOICES,
        default=PAYMENT_STATUS_PENDING
    )

    def __str__(self) -> str:
        return self.customer


class CartItem(models.Model):
    product = models.ForeignKey(ProductAndService, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', null=True)

    def __str__(self) -> str:
        return self.id

    class Meta:
        unique_together = [['cart', 'product']]


