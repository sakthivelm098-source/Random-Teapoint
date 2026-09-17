from django.db import models


class Product(models.Model):

    CATEGORY_CHOICES = [
        ("Tea", "Tea"),
        ("Coffee", "Coffee"),
        ("Breakfast", "Breakfast"),
        ("Snacks", "Snacks"),
        ("Cool Drinks", "Cool Drinks"),
        ("Specials", "Specials"),
    ]

    name = models.CharField(max_length=100)

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    tag = models.CharField(
        max_length=50,
        blank=True
    )

    image = models.URLField(
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    available = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.name