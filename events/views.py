from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Event


def event_list(request):
    """Events list view with pagination"""
    events_queryset = Event.objects.filter(is_active=True)
    paginator = Paginator(events_queryset, 6)

    page_number = request.GET.get('page')
    events = paginator.get_page(page_number)

    return render(request, 'events_list.html', {'events': events})


def event_detail(request, event_id):
    """Event detail view with media gallery"""
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events_detail.html', {'event': event})
