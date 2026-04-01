from django.shortcuts import render
from .models import ResultCategory, ResultFile


def result_list(request):
    categories = ResultCategory.objects.prefetch_related('files__subcategory').all()
    has_dynamic = ResultFile.objects.exists()
    return render(request, 'results_list.html', {
        'categories': categories,
        'has_dynamic': has_dynamic,
    })
