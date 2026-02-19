from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Program


def program_list(request):
    """Programs list view with pagination"""
    programs_queryset = Program.objects.filter(is_active=True)
    paginator = Paginator(programs_queryset, 8)  # 8 items per page

    page_number = request.GET.get('page')
    programs = paginator.get_page(page_number)

    context = {
        'programs': programs
    }
    return render(request, 'programs_list.html', context)


def program_detail(request, slug):
    """Program detail view"""
    program = get_object_or_404(Program, slug=slug, is_active=True)
    context = {
        'program': program
    }
    return render(request, 'program_detail.html', context)
