from datetime import date, timedelta
import time
from django.shortcuts import render, get_object_or_404
from django.db.models import Max, Q

from base.models import Article, Category

MAX_ITEMS_MAIN = 8

def get_sorted_articles():
    return Article.objects.order_by('-date', '-rebelion_id', '-id')

def get_daily_articles(timestamp):
    return get_sorted_articles().filter(day_timestamp=timestamp)

def get_latest_past_non_empty_day(potential):
    timestamp = time.mktime(potential.timetuple())
    articles = get_daily_articles(timestamp)
    return articles if len(articles) else get_latest_past_non_empty_day(potential - timedelta(days=1))

def get_grouped_categories():
    categories = Category.objects.all().order_by('name')
    return {
        'subjects': categories.filter(is_region=False),
        'countries': categories.filter(is_region=True, is_latin_america=False),
        'lacountries': categories.filter(is_latin_america=True),
    }

def index(request):
    articles = get_latest_past_non_empty_day(date.today())
    return render(request, 'front/index.html', {
        'today': articles,
        'categories': get_grouped_categories(),
    })

def article(request, article_id, article_slug):
    article = get_object_or_404(Article, id=article_id, slug=article_slug)
    return render(request, 'front/article.html', {
        'article': article,
        'categories': get_grouped_categories(),
    })

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    articles = get_sorted_articles().filter(category=category)[:20]

    return render(request, 'front/category.html', {
        'category': category,
        'articles': articles,
        'categories': get_grouped_categories(),
    })