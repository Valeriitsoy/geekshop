import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
import json
import os
import datetime
from geekshop.settings import BASE_DIR

from mainapp.models import Product, ProductCategory

from basketapp.models import Basket


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_product(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).\
        exclude(pk=hot_product.pk)[:3]

    return same_products


def main(request):
    products_1 = Product.objects.all()[:3]
    context = {
        'title': 'главная',
        'products': products_1,
        'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None, page=1):
    title = 'продукты'
    same_products = []
    same_products_file_path = os.path.join(BASE_DIR, 'same_products.json')
    if os.path.exists(same_products_file_path):
        with open(same_products_file_path, encoding='UTF-8') as products_file:
            same_products = json.loads(products_file.read())

    links_menu = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            category = {
                'pk': 0,
                'name': 'все'
            }
            products = Product.objects.all().order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk, is_active=True).order_by('price')

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
            'basket': get_basket(request.user),
        }
        return render(request, 'mainapp/products_list.html', context)
    hot_product = get_hot_product()
    # submenu = get_same_product(hot_product)
    context = {
        'title': title,
        'same_products': same_products,
        # 'submenu': submenu,
        'links_menu': links_menu,
        'basket': get_basket(request.user),
        'hot_product': hot_product
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    date_time = datetime.datetime.now()
    context = {
        'title': 'контакты',
        'date': date_time,
        'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/contact.html', context)


def product(request, pk):
    context = {
        'title': 'продукты',
        'basket': get_basket(request.user),
        'product': get_object_or_404(Product, pk=pk),
        'links_menu': ProductCategory.objects.all()
    }
    return render(request, 'mainapp/product.html', context)
