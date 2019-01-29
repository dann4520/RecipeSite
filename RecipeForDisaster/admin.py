from django.contrib import admin

from .models import Recipe, Ingredient


class ChoiceInline(admin.TabularInline):
    model = Ingredient
    extra = 3


class RecipeAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('name',)


admin.site.register(Recipe, RecipeAdmin)
