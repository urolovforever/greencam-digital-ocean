from django.shortcuts import render
from django.core.paginator import Paginator
from itertools import chain
from .models import Gallery
from news.models import NewsMedia
from events.models import EventMedia


def gallery_list(request):
    """Gallery page view displaying all media from gallery, news, and events"""
    source_filter = request.GET.get('source', 'all')

    # Gallery items
    gallery_items = Gallery.objects.all().values_list(
        'id', 'media_type', 'file', 'caption', 'created_at'
    )
    gallery_list = [
        {'media_type': g[1], 'file_url': g[2], 'caption': g[3], 'created_at': g[4], 'source': 'gallery'}
        for g in gallery_items
    ]

    # News media
    news_items = NewsMedia.objects.select_related('news').filter(news__is_published=True).values_list(
        'id', 'media_type', 'file', 'caption', 'news__created_at'
    )
    news_list = [
        {'media_type': n[1], 'file_url': n[2], 'caption': n[3], 'created_at': n[4], 'source': 'news'}
        for n in news_items
    ]

    # Events media
    event_items = EventMedia.objects.select_related('event').filter(event__is_active=True).values_list(
        'id', 'media_type', 'file', 'caption', 'event__created_at'
    )
    event_list = [
        {'media_type': e[1], 'file_url': e[2], 'caption': e[3], 'created_at': e[4], 'source': 'event'}
        for e in event_items
    ]

    # Filter by source
    if source_filter == 'gallery':
        all_media = gallery_list
    elif source_filter == 'news':
        all_media = news_list
    elif source_filter == 'events':
        all_media = event_list
    else:
        all_media = list(chain(gallery_list, news_list, event_list))

    # Sort by date (newest first)
    all_media.sort(key=lambda x: x['created_at'], reverse=True)

    paginator = Paginator(all_media, 12)
    page_number = request.GET.get('page')
    media_page = paginator.get_page(page_number)

    context = {
        'gallery_items': media_page,
        'current_source': source_filter,
    }
    return render(request, 'gallery.html', context)
