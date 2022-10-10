import json
import time

from django.shortcuts import render
import os
import requests
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from getData.Serializer import SerializerProduct, SerializerCategory, SerializerSUBCategory
from getData.models import Products, CategorysProduct, Subcatigory

auth = 'ae69c417856e4831a2f3429a87400757'
black_list = [
    '0f0ace85-ad1c-49ca-a4e3-c2ad524ec043',
    '3ed6d203-d2cc-4218-935e-d7b5876a1930',
]
list_subcategory = []


def loadAPI_categorys():
    CategorysProduct.objects.all().delete()
    Subcatigory.objects.all().delete()
    url = 'https://api.loyverse.com/v1.0/categories'
    result = requests.get(url, headers={'Authorization': 'Bearer ' + auth}).json()
    for category in result['categories']:
        for sub in list_subcategory:
            if (sub.split('|')[0] == category['id']):
                a = Subcatigory(
                    _id=sub.split('|')[0],
                    name=sub.split('|')[1]
                )
                a.save()
        category_bd = CategorysProduct(
            id_category=category['id'],
            name_category=category['name'],
        )
        if (not (category['id'] in black_list)):
            category_bd.save()


def stack():
    for product in Products.objects.all():
        time.sleep(0.2)
        print(product.idProduct)
        url = 'https://api.loyverse.com/v1.0/items?items_ids=' + product.idProduct
        res = requests.get(url, headers={'Authorization': 'Bearer ' + auth}).json()
        if (res['items'][0]['track_stock'] == True):
            try:
                url_st = 'https://api.loyverse.com/v1.0/inventory?variant_ids=' + product.idV
                res_st = requests.get(url_st, headers={'Authorization': 'Bearer ' + auth}).json()
                a = Products.objects.get(idV=product.idV)
                a.amounts = res_st['inventory_levels'][0]['in_stock']
                a.save(update_fields=['amounts'])
            except:
                a = Products.objects.get(idV=product.idV)
                a.amounts = -1
                a.save(update_fields=['amounts'])
        else:
            a = Products.objects.get(idV=product.idV)
            a.amounts = -1
            a.save(update_fields=['amounts'])

def loadAPI_products(cur):
    url = 'https://api.loyverse.com/v1.0/items?limit=250&cursor=' + cur
    res = requests.get(url, headers={'Authorization': 'Bearer ' + auth, "cursor": "string"}).json()
    for product in res['items']:
        if (product['variants'][0]['stores'][0]['price'] == None):
            price = 10
        else:
            price = product['variants'][0]['stores'][0]['price']
        if (product['image_url'] == None):
            img = 'https://cdn-icons-png.flaticon.com/512/4054/4054617.png'
        else:
            img = product['image_url']
        if (product['description'] == None):
            desc = ''
            sub_category = ''
        else:
            desc = product['description']
            sub_category = (product['description'].split('<p>|')[1]).split('|</p>')[0]
            if (not (product['category_id'] + '|' + sub_category in list_subcategory)):
                list_subcategory.append(product['category_id'] + '|' + sub_category)

        product_bd = Products(
            name=product['item_name'],
            description=desc,
            image=img,
            price=price,
            idProduct=product['id'],
            idCategory=product['category_id'],
            name_subcategory=sub_category,
            amounts=0,
            idV=product['variants'][0]['variant_id']
        )
        if (not (product['category_id'] in black_list) & (not (product['category_id'] in Products.objects.all()))):
            product_bd.save()
    if 'cursor' in res:
        return loadAPI_products(res['cursor'])


def loadAPI_product(request):
    stack()
    # Products.objects.all().delete()
    # loadAPI_products('')
    # loadAPI_categorys()
    return render(request, 'index.html')


def indexData(request):
    str = 'bdd837a9-fd85-4466-93bc-504934196007|Жвачка'
    head_tail = str.split('|')
    print(head_tail)
    return render(request, 'shop.html')


def paginationProducts(PageNumberPagination):
    page_size = 40
    page_size_query_param = 'page_size'
    max_page_size = 10000


def paginationCategory(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 10000


class PronuctsView(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = SerializerProduct
    pagination_class = PageNumberPagination


class PurchaseList(generics.ListAPIView):
    serializer_class = SerializerProduct

    def get_queryset(self):
        queryset = Products.objects.all()
        category = self.request.query_params.get('category'),
        subcategory = self.request.query_params.get('sub')
        if category is not None:
            queryset = queryset.filter(name_subcategory=subcategory)
        return queryset


class CategoryView(ModelViewSet):
    queryset = CategorysProduct.objects.all()
    serializer_class = SerializerCategory
    pagination_class = paginationCategory


class SubcategoryView(ModelViewSet):
    queryset = Subcatigory.objects.all()
    serializer_class = SerializerSUBCategory
    pagination_class = paginationCategory
