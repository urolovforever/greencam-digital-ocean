from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from programs.models import Program
from news.models import News
from events.models import Event
from partners.models import Partner
from .models import Material, AboutContent, AboutImage


def home(request):
    """Home page view"""
    featured_programs = Program.objects.filter(is_active=True, is_featured=True).order_by('-created_at')[:4]
    featured_news = News.objects.filter(is_published=True, is_featured=True).order_by('-created_at')[:3]
    featured_events = Event.objects.filter(is_active=True, is_featured=True).order_by('-created_at')[:3]
    partners = Partner.objects.filter(is_active=True)

    about_image = AboutImage.objects.filter(is_featured=True).first()
    about_content = AboutContent.objects.filter(page='home').first()

    context = {
        'programs': featured_programs,
        'news_list': featured_news,
        'events': featured_events,
        'partners': partners,
        'about_image': about_image,
        'about_content': about_content,
    }
    return render(request, 'home.html', context)


def about(request):
    """About page view"""
    images = AboutImage.objects.all()
    about_content = AboutContent.objects.filter(page='about').first()
    return render(request, 'about.html', {'about_images': images, 'about_content': about_content})


def faq(request):
    """FAQ page view"""
    return render(request, 'faq.html')


def privacy(request):
    """Privacy policy page view"""
    return render(request, 'privacy.html')


def terms(request):
    """Terms of use page view"""
    return render(request, 'terms.html')


def materials(request):
    """Materials page view with downloadable files"""
    materials = Material.objects.all()
    return render(request, 'materials.html', {'materials': materials})


def download_material(request, pk):
    """Download a material file"""
    material = get_object_or_404(Material, pk=pk)
    response = FileResponse(material.file.open('rb'), as_attachment=True)
    response['Content-Disposition'] = f'attachment; filename="{material.file.name.split("/")[-1]}"'
    return response
