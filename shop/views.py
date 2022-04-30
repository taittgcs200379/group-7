from django.shortcuts import render, redirect
from asyncio.windows_events import NULL
from .models import Category, Store
from .forms import CategoryForm, StoreForm

# Create your views here.
def category_index(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "category/index.html", context)


def category_details(request, id):
    category = Category.objects.get(id=id)
    context = {"category": category}
    return render(request, "category/details.html", context)


def category_delete(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect(category_index)


def category_add(request):
    form = CategoryForm(request.POST or None)

    if form.is_valid():
        category = Category()

        category.name = request.POST["name"]
        category.description = request.POST["description"]

        category.save()

        return redirect(category_index)

    context = {"form": form}

    return render(request, "category/add.html", context)


def category_edit(request, id):
    category = Category.objects.get(id=id)
    form = CategoryForm(request.POST or None, instance=category)

    if form.is_valid():
        category.name = request.POST["name"]
        category.description = request.POST["description"]

        form.save()

        return redirect(category_index)

    context = {"form": form}

    return render(request, "category/edit.html", context)


def back_to_categorylist(request):
    return redirect(category_index)


#CRUDShop
def store_index(request):
    stores = Store.objects.all()
    categories = Category.objects.all()
    context = {
        "stores":  stores,
        "categories": categories,
    }
    return render(request, "store/index.html", context)

def store_details(request, id):
    store = Store.objects.get(id=id)
    context = {
        "store": store,
    }
    return render(request, "store/details.html", context)

def store_delete(request, id):
    store = Store.objects.get(id=id)
    store.delete()
    return redirect(store_index)

def store_add(request):
    form = StoreForm(request.POST or None)

    if form.is_valid():
       
       store = Store()

       store.image = request.POST["image"]
       store.description = request.POST["description"]
       store.code = request.POST["code"]
       store.name = request.POST["name"]
       store.date = request.POST["date"]
       store.price = request.POST["price"]
        

       category = Category.objects.get(id=int(request.POST["category"]))
       store.category = category

       store.save()

       return redirect(store_index)

    context = {"form": form}

    return render(request, "store/add.html", context)


def store_edit(request, id):
    store = Store.objects.get(id=id)
    form = StoreForm(request.POST or None)

    if form.is_valid():
       
      
       store.image = request.POST["image"]
       store.description = request.POST["description"]
       store.code = request.POST["code"]
       store.name = request.POST["name"]
       store.date = request.POST["date"]
       store.price = request.POST["price"]
        

       category = Category.objects.get(id= int(request.POST["category"]))
       store.category = category

       form.save()

       return redirect(store_index)

    context = {"form": form}

    return render(request, "store/edit.html", context)

def back_to_storelist(request):
    return redirect(store_index)

def show_category(request, category_id):
    category = Category.objects.get(id=category_id)
    stores = Store.objects.filter(category=category)
    categories = Category.objects.all()
    context = {
        "stores":  stores,
        "categories": categories,

    }
    return render(request, "store/index.html", context)

