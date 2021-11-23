from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Names_tags


class Names_tagsInlineFormset(BaseInlineFormSet):
    def clean(self):
        check_list = []
        count = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data['is_main'] is True:
                count = count + 1
                check_list.append(count)
        if len(check_list) > 1:
            raise ValidationError('Основной тег может быть только один для статьи')
        else:
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            # raise ValidationError('Тут всегда ошибка')
            return super().clean()  # вызываем базовый код переопределяемого метода


class Names_tagsInline(admin.TabularInline):
    model = Names_tags
    extra = 0
    formset = Names_tagsInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [Names_tagsInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [Names_tagsInline]


@admin.register(Names_tags)
class Names_tagsAdmin(admin.ModelAdmin):
    list_display = ['article', 'tag', 'is_main']
    pass
