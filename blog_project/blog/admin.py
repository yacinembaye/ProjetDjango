from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_publication')
    list_filter = ('date_publication', 'auteur')
    search_fields = ('titre', 'contenu')
    date_hierarchy = 'date_publication'