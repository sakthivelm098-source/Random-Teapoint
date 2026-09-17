from django.shortcuts import render

from .models import Product


def home(request):

    products = Product.objects.filter(
        available=True
    )

    categories = [
        "Tea",
        "Coffee",
        "Breakfast",
        "Snacks",
        "Cool Drinks",
        "Specials"
    ]

    context = {

        "shop_name": "Orange Leaf Café",

        "point_name": "Tea Point",

        "categories": categories,

        "products": products,

    }

    return render(
        request,
        "tea/home.html",
        context
    )
