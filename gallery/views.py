from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Gallery


def gallery_list(request):
    gallery_items = Gallery.objects.all().order_by('-created_at')
    paginator = Paginator(gallery_items, 12)
    page_number = request.GET.get('page')
    media_page = paginator.get_page(page_number)
    return render(request, 'gallery.html', {'gallery_items': media_page})
