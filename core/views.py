from django.shortcuts import render
from programs.views import WP_DATA, _get_wp_translated
from news.models import News
from events.models import Event
from partners.models import Partner
from gallery.models import Gallery


def home(request):
    featured_news = News.objects.filter(is_published=True).order_by('-created_at')[:3]
    featured_events = Event.objects.filter(is_active=True).order_by('-date')[:3]
    partners = Partner.objects.filter(is_active=True)
    gallery_photos = Gallery.objects.filter(media_type='image').order_by('-created_at')[:6]
    wp_list = [_get_wp_translated(wp) for wp in list(WP_DATA.values())[:3]]

    return render(request, 'home.html', {
        'wp_list': wp_list,
        'news_list': featured_news,
        'events': featured_events,
        'partners': partners,
        'gallery_photos': gallery_photos,
    })


def about(request):
    return render(request, 'about.html')


def partners_page(request):
    return render(request, 'partners_page.html')


def faq(request):
    return render(request, 'faq.html')


def privacy(request):
    return render(request, 'privacy.html')


def terms(request):
    return render(request, 'terms.html')
