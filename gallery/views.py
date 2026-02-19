from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Gallery


def gallery_list(request):
    """Gallery page view displaying all gallery images with pagination"""
    gallery_queryset = Gallery.objects.all()
    paginator = Paginator(gallery_queryset, 12)  # 12 items per page

    page_number = request.GET.get('page')
    gallery_images = paginator.get_page(page_number)

    context = {
        'gallery_images': gallery_images,
    }
    return render(request, 'gallery.html', context)
