from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.db import IntegrityError
from .models import Event, Registration
from .forms import RegistrationForm


def event_list(request):
    """Events list view with pagination"""
    events_queryset = Event.objects.all()
    paginator = Paginator(events_queryset, 6)  # 6 items per page

    page_number = request.GET.get('page')
    events = paginator.get_page(page_number)

    context = {
        'events': events
    }
    return render(request, 'events_list.html', context)


def event_detail(request, event_id):
    """Event detail view with registration form"""
    event = get_object_or_404(Event, pk=event_id)

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                registration = form.save(commit=False)
                registration.event = event
                registration.save()
                messages.success(request, f'Successfully registered for {event.name}!')
                return redirect('events:list')
            except IntegrityError:
                messages.error(request, 'You have already registered for this event with this email.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegistrationForm()

    context = {
        'event': event,
        'form': form
    }
    return render(request, 'events_detail.html', context)
