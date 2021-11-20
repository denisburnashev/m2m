from django.shortcuts import render

from articles.models import Article, Tag, Names_tags


def articles_list(request):
    template = 'articles/news.html'
    # articles = Article.objects.prefetch_related('tags')
    articles = Article.objects.prefetch_related('scopes')
    print(articles)
    # for article in articles:
    #     for scope in article.scopes.all():
    #         for is_main in scope.to_tag.all():
    #             print(is_main.main)
    #             if is_main.main is True:
    #                 print('Основной')
    context = {'object_list': articles}
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
