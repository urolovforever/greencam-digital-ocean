from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import News


def news_list(request):
    """News list view with pagination"""
    news_queryset = News.objects.filter(is_published=True)
    paginator = Paginator(news_queryset, 6)  # 6 items per page

    page_number = request.GET.get('page')
    news_list = paginator.get_page(page_number)

    context = {
        'news_list': news_list
    }
    return render(request, 'news_list.html', context)


def news_detail(request, slug):
    """News detail view"""
    news = get_object_or_404(News, slug=slug, is_published=True)
    context = {
        'news': news
    }
    return render(request, 'news_detail.html', context)
