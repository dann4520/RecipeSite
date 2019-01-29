from django.shortcuts import render
from django.utils import timezone
from .models import Recipe

# Create your views here.
def recipe_list(request):
    recipes = Recipe.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'RecipeForDisaster/recipe_list.html', {'recipes': recipes})


