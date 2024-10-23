from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404

from recipes.models import Recipe

# Create your views here.

# HTTP REQUEST
def home(request):
    # HTTP RESPONSE
    recipes = Recipe.objects.filter(
       is_published=True,
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })

 
def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })


def category(request, category_id):
    # HTTP RESPONSE
    recipes = get_list_or_404(
        Recipe.objects.filter(
        category__id=category_id,
        is_published=True
        ).order_by('-id')
    )
    
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category'
    })