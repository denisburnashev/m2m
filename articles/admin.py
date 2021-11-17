from django.contrib import admin

from .models import Article, Tag, Names_tags


class Names_tagsInline(admin.TabularInline):
    model = Names_tags


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [Names_tagsInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [Names_tagsInline]


@admin.register(Names_tags)
class Names_tagsAdmin(admin.ModelAdmin):
    pass
