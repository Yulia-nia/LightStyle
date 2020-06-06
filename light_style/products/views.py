from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET

from products.models import Product, Category


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print(request.session.session_key)
    return render(request, 'products/retrieve.html', locals())


'''def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, '/products/retrieve.html', {'product': product,
                                                        'cart_product_form': cart_product_form})
'''

@require_GET
def catalog(request, category_slug=None):
    query = request.GET.get('q', '')
    products = Product.objects.filter(
        Q(name__contains=query) | Q(description__contains=query) | Q(category__name__contains=query)
    )
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'products.html', context={'category': category,
                   'categories': categories, 'products': products})


def retrieve(request, id=None):
    product = Product.objects.get(pk=id)
    return render(request, 'retrieve.html', context={'product': product})

