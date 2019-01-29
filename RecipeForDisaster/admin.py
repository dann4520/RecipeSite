from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Recipe, Ingredient
'''
admin.site.register(Recipe)
admin.site.register(Ingredient)

'''
class ChoiceInline(admin.TabularInline):
    model = Ingredient
    extra = 3

class RecipeAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('name',)
admin.site.register(Recipe, RecipeAdmin)