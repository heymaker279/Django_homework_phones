from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_dict = {'max_price': '-price', 'min_price': 'price', 'name': 'name'}
    template = 'catalog.html'
    phones = Phone.objects.all()
    if request.GET.get('sort') in sort_dict:
        phones = Phone.objects.all().order_by(sort_dict[f'{request.GET.get("sort")}'])
    context = {'phones': phones}
    return render(request, template, context)



def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
