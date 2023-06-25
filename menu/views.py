from django.shortcuts import redirect, reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
# from .forms import ReviewForm
from .models import MenuItem, Category  # Add import for Category model
from .forms import MenuForm


def menu_list(request):
    if request.user.is_superuser:  # Check if user is an admin
        menu_items = MenuItem.objects.all()
    else:
        menu_items = MenuItem.objects.filter(status='approved')

    menu_items_by_category = {}  # Dictionary to store menu items by category

    # Retrieve all menu items and group them by category
    categories = Category.objects.all()
    for category in categories:
        category_menu_items = menu_items.filter(category=category)
        menu_items_by_category[category] = category_menu_items

    context = {'menu_items_by_category': menu_items_by_category}
    return render(request, 'menu/menu_list.html', context)


def add_menu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to menu-list URL name
            return redirect(reverse('menu-list'))
    form = MenuForm()
    context = {
        'form': form
    }
    return render(request, 'menu/add_menu.html', context)


def edit_menu(request, menu_item_id):
    item = get_object_or_404(MenuItem, id=menu_item_id)
    form = MenuForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'menu/edit_menu.html', context)


def hide_menu(request, menu_item_id):
    menu_item = get_object_or_404(MenuItem, id=menu_item_id)
    menu_item.status = 'draft'
    menu_item.save()
    return redirect(reverse('menu-list'))


def delete_menu(request, menu_item_id):
    menu_item = get_object_or_404(MenuItem, id=menu_item_id)
    menu_item.delete()
    return redirect(reverse('menu-list'))
