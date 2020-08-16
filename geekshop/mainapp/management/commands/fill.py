import json
import os

from django.core.management import BaseCommand

from mainapp.models import ProductCategory, Product

from authapp.models import ShopUser


def load_json(file_name):
    with open(os.path.join('mainapp/json', file_name + '.json'), encoding='UTF-8') as json_file:
        return json.load(json_file)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        categories = load_json('categories')
        ProductCategory.objects.all().delete()
        # cats_dict = dict()

        for cat in categories:
            new_cat = ProductCategory(**cat)
            new_cat.save()
            # cats_dict[cat['name']] = new_cat.id

        products = load_json('products')
        Product.objects.all().delete()

        for product in products:
            category_item = ProductCategory.objects.get(name=product['category'])
            # product['category_id'] = cats_dict[product['category']]
            product['category'] = category_item
            new_prod = Product(**product)
            new_prod.save()

        super_user = ShopUser.objects.create_superuser(
            'django',
            'django@geekbrains.local',
            'geekbrains',
            age=34
        )
