from multiprocessing import context
from django.shortcuts import redirect, render

from product.models import Product

from .forms import CreateProductForm

# Create your views here.



def list_product_view(request):
    template_name="products/index.html"
    product = Product.objects.all()
    context={
        'product':product
    }
    return render(request,template_name,context)


def create_product_view(request):
    template_name='products/create.html'
  
    form =CreateProductForm(request.POST)
    context={'form':form}
    if form.is_valid():
        form.save()
    return render(request,template_name,context)


def delete_product_view(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('product:product_list')