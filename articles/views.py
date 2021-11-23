from django.shortcuts import render

from articles.models import Article, Tag, Names_tags


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.prefetch_related('scopes')
    context = {'object_list': articles}
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
